import psycopg2
import getpass

# ============================================================
# DATABASE CONFIGURATION
# ============================================================

print("============================================================")
print("             SOIL ANALYSIS HISTORY")
print("============================================================")

password = getpass.getpass("Enter PostgreSQL password: ")

try:

    # ========================================================
    # CONNECT TO POSTGRESQL
    # ========================================================

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="soil_analytics",
        user="postgres",
        password=password
    )

    cursor = conn.cursor()

    print("\nPostgreSQL connected successfully!")

    # ========================================================
    # GET ALL SOIL SAMPLES
    # ========================================================

    cursor.execute("""
        SELECT
            sample_id,
            sample_date,
            soil_type,
            nitrogen,
            phosphorus,
            potassium,
            ph,
            soil_moisture,
            organic_matter,
            temperature,
            humidity,
            rainfall
        FROM soil_samples
        ORDER BY sample_id DESC;
    """)

    samples = cursor.fetchall()

    if not samples:

        print("\nNo soil analysis records found.")

    else:

        print(f"\nTotal soil samples found: {len(samples)}")

        # ====================================================
        # DISPLAY EACH SAMPLE
        # ====================================================

        for sample in samples:

            (
                sample_id,
                sample_date,
                soil_type,
                nitrogen,
                phosphorus,
                potassium,
                ph,
                soil_moisture,
                organic_matter,
                temperature,
                humidity,
                rainfall
            ) = sample

            print("\n============================================================")
            print(f"                 SAMPLE ID: {sample_id}")
            print("============================================================")

            print("\nSOIL SAMPLE")
            print("------------------------------------------------------------")
            print(f"Date:             {sample_date}")
            print(f"Soil Type:        {soil_type}")
            print(f"Nitrogen (N):     {nitrogen}")
            print(f"Phosphorus (P):   {phosphorus}")
            print(f"Potassium (K):    {potassium}")
            print(f"pH:               {ph}")
            print(f"Soil Moisture:    {soil_moisture}")
            print(f"Organic Matter:   {organic_matter}")
            print(f"Temperature:      {temperature}")
            print(f"Humidity:         {humidity}")
            print(f"Rainfall:         {rainfall}")

            # =================================================
            # NUTRIENT PREDICTIONS
            # =================================================

            cursor.execute("""
                SELECT
                    nitrogen_status,
                    nitrogen_probability,
                    phosphorus_status,
                    phosphorus_probability,
                    potassium_status,
                    potassium_probability
                FROM nutrient_predictions
                WHERE sample_id = %s;
            """, (sample_id,))

            prediction = cursor.fetchone()

            print("\nNUTRIENT PREDICTION")
            print("------------------------------------------------------------")

            if prediction:

                (
                    nitrogen_status,
                    nitrogen_probability,
                    phosphorus_status,
                    phosphorus_probability,
                    potassium_status,
                    potassium_probability
                ) = prediction

                print(f"Nitrogen:")
                print(f"  Status: {nitrogen_status}")
                print(f"  Deficiency Probability: {nitrogen_probability:.2f}%")

                print(f"\nPhosphorus:")
                print(f"  Status: {phosphorus_status}")
                print(f"  Deficiency Probability: {phosphorus_probability:.2f}%")

                print(f"\nPotassium:")
                print(f"  Status: {potassium_status}")
                print(f"  Deficiency Probability: {potassium_probability:.2f}%")

            else:

                print("No nutrient prediction found.")

            # =================================================
            # SOIL ASSESSMENT
            # =================================================

            cursor.execute("""
                SELECT
                    soil_health_score,
                    soil_health_status,
                    primary_nutrient_concern
                FROM soil_assessment
                WHERE sample_id = %s;
            """, (sample_id,))

            assessment = cursor.fetchone()

            print("\nHYBRID SOIL ASSESSMENT")
            print("------------------------------------------------------------")

            if assessment:

                (
                    soil_health_score,
                    soil_health_status,
                    primary_nutrient_concern
                ) = assessment

                print(f"Health Score:              {soil_health_score}")
                print(f"Health Status:             {soil_health_status}")
                print(f"Primary Nutrient Concern:  {primary_nutrient_concern}")

            else:

                print("No soil assessment found.")

            # =================================================
            # CROP ADVISORY
            # =================================================

            cursor.execute("""
                SELECT
                    crop_name,
                    recommendation_reason
                FROM crop_advisory
                WHERE sample_id = %s
                ORDER BY advisory_id;
            """, (sample_id,))

            crops = cursor.fetchall()

            print("\nCROP ADVISORY")
            print("------------------------------------------------------------")

            if crops:

                for i, crop in enumerate(crops, start=1):

                    crop_name = crop[0]
                    reason = crop[1]

                    print(f"{i}. {crop_name}")
                    print(f"   Reason: {reason}")

            else:

                print("No crop advisory found.")

    # ========================================================
    # CLOSE DATABASE
    # ========================================================

    cursor.close()
    conn.close()

    print("\n============================================================")
    print("           SOIL HISTORY RETRIEVAL COMPLETED")
    print("============================================================")

except Exception as e:

    print("\n============================================================")
    print("             DATABASE ERROR")
    print("============================================================")
    print("Error:", e)

    try:
        cursor.close()
        conn.close()
    except:
        pass