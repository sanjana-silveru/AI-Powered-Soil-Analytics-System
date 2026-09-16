import psycopg2
import getpass
from datetime import date

# ==============================
# PostgreSQL Configuration
# ==============================

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "soil_analytics",
    "user": "postgres"
}

# ==============================
# Get PostgreSQL Password
# ==============================

password = getpass.getpass("Enter PostgreSQL password: ")
DB_CONFIG["password"] = password


try:
    # Connect to database
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    print("\nPostgreSQL connected successfully!")

    # ==============================
    # Sample Hybrid Analysis Result
    # ==============================

    soil_type = "Black Soil"

    nitrogen_status = "SUFFICIENT"
    nitrogen_probability = 3.11

    phosphorus_status = "SUFFICIENT"
    phosphorus_probability = 5.08

    potassium_status = "DEFICIENT"
    potassium_probability = 98.56

    # Soil health score
    deficiencies = 1

    if deficiencies == 0:
        soil_health_status = "GOOD"
    elif deficiencies == 1:
        soil_health_status = "NEEDS IMPROVEMENT"
    elif deficiencies == 2:
        soil_health_status = "POOR"
    else:
        soil_health_status = "CRITICAL"

    primary_nutrient_concern = "Potassium"

    # ==============================
    # Insert Soil Sample
    # ==============================

    cursor.execute("""
        INSERT INTO soil_samples
        (
            sample_date,
            soil_type,
            nitrogen,
            phosphorus,
            potassium
        )
        VALUES (%s, %s, %s, %s, %s)
        RETURNING sample_id;
    """, (
        date.today(),
        soil_type,
        50,
        40,
        50
    ))

    sample_id = cursor.fetchone()[0]

    print("Soil sample saved. Sample ID:", sample_id)

    # ==============================
    # Insert Nutrient Predictions
    # ==============================

    cursor.execute("""
        INSERT INTO nutrient_predictions
        (
            sample_id,
            nitrogen_status,
            nitrogen_probability,
            phosphorus_status,
            phosphorus_probability,
            potassium_status,
            potassium_probability
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (
        sample_id,
        nitrogen_status,
        nitrogen_probability,
        phosphorus_status,
        phosphorus_probability,
        potassium_status,
        potassium_probability
    ))

    print("Nutrient predictions saved.")

    # ==============================
    # Insert Soil Assessment
    # ==============================

    soil_health_score = 100 - (deficiencies * 25)

    cursor.execute("""
        INSERT INTO soil_assessment
        (
            sample_id,
            soil_health_score,
            soil_health_status,
            primary_nutrient_concern
        )
        VALUES (%s, %s, %s, %s);
    """, (
        sample_id,
        soil_health_score,
        soil_health_status,
        primary_nutrient_concern
    ))

    print("Soil assessment saved.")

    # Save everything
    conn.commit()

    print("\n===================================")
    print("HYBRID RESULT SAVED SUCCESSFULLY")
    print("===================================")
    print("Sample ID:", sample_id)
    print("Soil Type:", soil_type)
    print("N:", nitrogen_status)
    print("P:", phosphorus_status)
    print("K:", potassium_status)
    print("Health Status:", soil_health_status)
    print("Primary Concern:", primary_nutrient_concern)

    cursor.close()
    conn.close()

except Exception as e:

    print("\nDatabase operation failed!")
    print("Error:", e)