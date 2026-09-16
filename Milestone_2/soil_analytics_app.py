import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import pandas as pd
import joblib
import psycopg2
from datetime import datetime


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="AI-Powered Soil Analytics",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_PATH = r"C:\Users\SILVERU SANJANA\OneDrive\Desktop\Soil_Project"

CNN_MODEL_PATH = (
    BASE_PATH +
    r"\CNN_Model\best_resnet50_soil_model.pth"
)

N_MODEL_PATH = (
    BASE_PATH +
    r"\Structured_Data\ML_Results"
    r"\best_nitrogen_deficiency_model.pkl"
)

P_MODEL_PATH = (
    BASE_PATH +
    r"\Structured_Data\ML_Results"
    r"\phosphorus_deficiency_model.pkl"
)

K_MODEL_PATH = (
    BASE_PATH +
    r"\Structured_Data\ML_Results"
    r"\potassium_deficiency_model.pkl"
)


# ============================================================
# SOIL CLASS NAMES
# ============================================================

CLASS_NAMES = [
    "Alluvial Soil",
    "Arid Soil",
    "Black Soil",
    "Laterite Soil",
    "Mountain Soil",
    "Red Soil",
    "Yellow Soil"
]


# ============================================================
# LOAD RESNET-50
# ============================================================

@st.cache_resource
def load_cnn_model():

    model = models.resnet50(weights=None)

    model.fc = nn.Linear(
        model.fc.in_features,
        7
    )

    state_dict = torch.load(
        CNN_MODEL_PATH,
        map_location="cpu"
    )

    model.load_state_dict(state_dict)

    model.eval()

    return model


# ============================================================
# LOAD NUTRIENT MODELS
# ============================================================

@st.cache_resource
def load_nutrient_models():

    nitrogen_model = joblib.load(
        N_MODEL_PATH
    )

    phosphorus_model = joblib.load(
        P_MODEL_PATH
    )

    potassium_model = joblib.load(
        K_MODEL_PATH
    )

    return (
        nitrogen_model,
        phosphorus_model,
        potassium_model
    )


# ============================================================
# IMAGE PREPROCESSING
# ============================================================

image_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ============================================================
# DATABASE CONNECTION FUNCTION
# ============================================================

def create_database_connection(password):

    return psycopg2.connect(
        host="localhost",
        database="soil_analytics",
        user="postgres",
        password=password
    )


# ============================================================
# TITLE
# ============================================================

st.title(
    "🌱 AI-Powered Soil Analytics System"
)

st.subheader(
    "Nutrient Assessment and Intelligent Crop Advisory"
)

st.caption(
    "ResNet-50 + Gradient Boosting + Hybrid Assessment + PostgreSQL"
)


# ============================================================
# SYSTEM ARCHITECTURE
# ============================================================

st.subheader("🏗️ System Architecture")

st.markdown(
    """
**Soil Image → ResNet-50 → Soil Type**

**Soil Parameters → Nutrient ML Models → Deficiency Risk**

**Measured N/P/K + ML Predictions → Hybrid Assessment → Soil Health**
"""
)

st.divider()


# ============================================================
# LOAD MODELS
# ============================================================

try:

    cnn_model = load_cnn_model()

    (
        nitrogen_model,
        phosphorus_model,
        potassium_model
    ) = load_nutrient_models()

    st.success(
        "✅ All AI/ML models loaded successfully."
    )

except Exception as error:

    st.error(
        "❌ Error loading AI/ML models."
    )

    st.code(str(error))

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "🗄️ PostgreSQL Database"
)

db_password = st.sidebar.text_input(
    "PostgreSQL Password",
    type="password"
)


# ============================================================
# DATABASE TEST
# ============================================================

if st.sidebar.button(
    "Test Database Connection"
):

    if not db_password:

        st.sidebar.warning(
            "Enter PostgreSQL password."
        )

    else:

        test_connection = None

        try:

            test_connection = create_database_connection(
                db_password
            )

            st.sidebar.success(
                "✅ PostgreSQL Connected"
            )

        except Exception as error:

            st.sidebar.error(
                "❌ PostgreSQL connection failed."
            )

            st.sidebar.code(
                str(error)
            )

        finally:

            if test_connection is not None:

                test_connection.close()


# ============================================================
# INPUT SECTION
# ============================================================

st.header(
    "📥 Soil Analysis Input"
)


# ============================================================
# SOIL IMAGE
# ============================================================

st.subheader(
    "1️⃣ Soil Image"
)

uploaded_file = st.file_uploader(
    "Upload a soil image",
    type=["jpg", "jpeg", "png"]
)


# ============================================================
# SOIL PARAMETERS
# ============================================================

st.subheader(
    "2️⃣ Soil Parameters"
)

col1, col2, col3 = st.columns(3)


with col1:

    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=500.0,
        value=50.0
    )

    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=500.0,
        value=40.0
    )

    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=500.0,
        value=50.0
    )


with col2:

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    soil_moisture = st.number_input(
        "Soil Moisture",
        min_value=0.0,
        max_value=100.0,
        value=20.0
    )

    organic_matter = st.number_input(
        "Organic Matter",
        min_value=0.0,
        max_value=100.0,
        value=5.0
    )


with col3:

    temperature = st.number_input(
        "Temperature",
        min_value=-20.0,
        max_value=100.0,
        value=25.0
    )

    humidity = st.number_input(
        "Humidity",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    rainfall = st.number_input(
        "Rainfall",
        min_value=0.0,
        max_value=1000.0,
        value=100.0
    )


# ============================================================
# ANALYZE
# ============================================================

analyze = st.button(
    "🔍 Analyze Soil",
    type="primary",
    use_container_width=True
)


# ============================================================
# MAIN ANALYSIS
# ============================================================

if analyze:

    if uploaded_file is None:

        st.warning(
            "⚠️ Please upload a soil image."
        )

    else:

        try:

            # =================================================
            # IMAGE
            # =================================================

            image = Image.open(
                uploaded_file
            ).convert("RGB")

            image_tensor = image_transform(
                image
            ).unsqueeze(0)


            # =================================================
            # RESNET-50 PREDICTION
            # =================================================

            with torch.no_grad():

                output = cnn_model(
                    image_tensor
                )

                probabilities = torch.softmax(
                    output,
                    dim=1
                )

                confidence, predicted_class = torch.max(
                    probabilities,
                    dim=1
                )

            soil_type = CLASS_NAMES[
                predicted_class.item()
            ]

            cnn_confidence = (
                float(confidence.item()) * 100
            )


            # =================================================
            # MEASURED NUTRIENT STATUS
            # =================================================

            nitrogen_measured = (
                "DEFICIENT"
                if nitrogen < 40
                else "SUFFICIENT"
            )

            phosphorus_measured = (
                "DEFICIENT"
                if phosphorus < 30
                else "SUFFICIENT"
            )

            potassium_measured = (
                "DEFICIENT"
                if potassium < 40
                else "SUFFICIENT"
            )


            # =================================================
            # NITROGEN ML INPUT
            # =================================================

            nitrogen_input = pd.DataFrame(
                [[
                    phosphorus,
                    potassium,
                    ph,
                    soil_moisture,
                    organic_matter,
                    temperature,
                    humidity,
                    rainfall
                ]],
                columns=[
                    "p",
                    "k",
                    "ph",
                    "soil_moisture",
                    "organic_matter",
                    "temperature",
                    "humidity",
                    "rainfall"
                ]
            )


            # =================================================
            # PHOSPHORUS ML INPUT
            # =================================================

            phosphorus_input = pd.DataFrame(
                [[
                    nitrogen,
                    potassium,
                    ph,
                    soil_moisture,
                    organic_matter,
                    temperature,
                    humidity,
                    rainfall
                ]],
                columns=[
                    "n",
                    "k",
                    "ph",
                    "soil_moisture",
                    "organic_matter",
                    "temperature",
                    "humidity",
                    "rainfall"
                ]
            )


            # =================================================
            # POTASSIUM ML INPUT
            # =================================================

            potassium_input = pd.DataFrame(
                [[
                    nitrogen,
                    phosphorus,
                    ph,
                    soil_moisture,
                    organic_matter,
                    temperature,
                    humidity,
                    rainfall
                ]],
                columns=[
                    "n",
                    "p",
                    "ph",
                    "soil_moisture",
                    "organic_matter",
                    "temperature",
                    "humidity",
                    "rainfall"
                ]
            )


            # =================================================
            # ML PREDICTIONS
            # =================================================

            nitrogen_prediction = int(
                nitrogen_model.predict(
                    nitrogen_input
                )[0]
            )

            phosphorus_prediction = int(
                phosphorus_model.predict(
                    phosphorus_input
                )[0]
            )

            potassium_prediction = int(
                potassium_model.predict(
                    potassium_input
                )[0]
            )


            # =================================================
            # ML PROBABILITIES
            # =================================================

            nitrogen_probability = float(
                nitrogen_model.predict_proba(
                    nitrogen_input
                )[0][1]
            )

            phosphorus_probability = float(
                phosphorus_model.predict_proba(
                    phosphorus_input
                )[0][1]
            )

            potassium_probability = float(
                potassium_model.predict_proba(
                    potassium_input
                )[0][1]
            )


            # =================================================
            # ML STATUS
            # =================================================

            nitrogen_ml = (
                "DEFICIENT"
                if nitrogen_prediction == 1
                else "SUFFICIENT"
            )

            phosphorus_ml = (
                "DEFICIENT"
                if phosphorus_prediction == 1
                else "SUFFICIENT"
            )

            potassium_ml = (
                "DEFICIENT"
                if potassium_prediction == 1
                else "SUFFICIENT"
            )


            # =================================================
            # HYBRID HEALTH
            # =================================================

            deficiencies = []

            if nitrogen_measured == "DEFICIENT":
                deficiencies.append(
                    "Nitrogen"
                )

            if phosphorus_measured == "DEFICIENT":
                deficiencies.append(
                    "Phosphorus"
                )

            if potassium_measured == "DEFICIENT":
                deficiencies.append(
                    "Potassium"
                )

            deficiency_count = len(
                deficiencies
            )


            if deficiency_count == 0:

                health_score = 100
                health_status = "GOOD"
                primary_concern = "None"

            elif deficiency_count == 1:

                health_score = 75
                health_status = "NEEDS IMPROVEMENT"
                primary_concern = deficiencies[0]

            elif deficiency_count == 2:

                health_score = 50
                health_status = "POOR"
                primary_concern = ", ".join(
                    deficiencies
                )

            else:

                health_score = 25
                health_status = "CRITICAL"
                primary_concern = ", ".join(
                    deficiencies
                )


            # =================================================
            # CROP ADVISORY
            # =================================================

            if soil_type == "Black Soil":

                crops = [
                    "Cotton",
                    "Soybean",
                    "Wheat"
                ]

            elif soil_type == "Red Soil":

                crops = [
                    "Groundnut",
                    "Millets",
                    "Pulses"
                ]

            elif soil_type == "Alluvial Soil":

                crops = [
                    "Rice",
                    "Wheat",
                    "Sugarcane"
                ]

            elif soil_type == "Arid Soil":

                crops = [
                    "Millets",
                    "Barley",
                    "Pulses"
                ]

            elif soil_type == "Laterite Soil":

                crops = [
                    "Cashew",
                    "Tea",
                    "Coffee"
                ]

            elif soil_type == "Mountain Soil":

                crops = [
                    "Potato",
                    "Tea",
                    "Barley"
                ]

            else:

                crops = [
                    "Millets",
                    "Pulses",
                    "Groundnut"
                ]


            # =================================================
            # DISPLAY SOIL TYPE
            # =================================================

            st.subheader(
                "1. Soil Type Classification"
            )

            image_col, result_col = st.columns(2)

            with image_col:

                st.image(
                    image,
                    caption="Uploaded Soil Image",
                    use_container_width=True
                )

            with result_col:

                st.success(
                    f"🌱 Soil Type: {soil_type}"
                )

                st.metric(
                    "CNN Confidence",
                    f"{cnn_confidence:.2f}%"
                )


            # =================================================
            # DISPLAY NUTRIENT ANALYSIS
            # =================================================

            st.subheader(
                "2. Nutrient Analysis"
            )

            n_col, p_col, k_col = st.columns(3)


            with n_col:

                st.markdown(
                    "### 🟢 Nitrogen"
                )

                st.write(
                    f"**Measured Status:** "
                    f"{nitrogen_measured}"
                )

                st.write(
                    f"**ML Deficiency Risk:** "
                    f"{nitrogen_ml}"
                )

                st.write(
                    f"**ML Probability:** "
                    f"{nitrogen_probability * 100:.2f}%"
                )


            with p_col:

                st.markdown(
                    "### 🟡 Phosphorus"
                )

                st.write(
                    f"**Measured Status:** "
                    f"{phosphorus_measured}"
                )

                st.write(
                    f"**ML Deficiency Risk:** "
                    f"{phosphorus_ml}"
                )

                st.write(
                    f"**ML Probability:** "
                    f"{phosphorus_probability * 100:.2f}%"
                )


            with k_col:

                st.markdown(
                    "### 🔴 Potassium"
                )

                st.write(
                    f"**Measured Status:** "
                    f"{potassium_measured}"
                )

                st.write(
                    f"**ML Deficiency Risk:** "
                    f"{potassium_ml}"
                )

                st.write(
                    f"**ML Probability:** "
                    f"{potassium_probability * 100:.2f}%"
                )


            # =================================================
            # HYBRID ASSESSMENT
            # =================================================

            st.subheader(
                "3. Hybrid Soil Assessment"
            )

            h1, h2, h3 = st.columns(3)

            with h1:

                st.metric(
                    "Soil Health Score",
                    f"{health_score}/100"
                )

            with h2:

                st.metric(
                    "Health Status",
                    health_status
                )

            with h3:

                st.metric(
                    "Deficiencies",
                    deficiency_count
                )

            st.write(
                f"**Primary Nutrient Concern:** "
                f"{primary_concern}"
            )

            st.info(
                "Measured Status is calculated using the "
                "project's defined N/P/K thresholds. "
                "ML Deficiency Risk is produced by the "
                "trained Gradient Boosting models."
            )


            # =================================================
            # DIFFERENCE WARNING
            # =================================================

            differences = []

            if nitrogen_measured != nitrogen_ml:
                differences.append(
                    "Nitrogen"
                )

            if phosphorus_measured != phosphorus_ml:
                differences.append(
                    "Phosphorus"
                )

            if potassium_measured != potassium_ml:
                differences.append(
                    "Potassium"
                )

            if differences:

                st.warning(
                    "⚠️ Measured and ML results differ for: "
                    + ", ".join(differences)
                )


            # =================================================
            # CROP ADVISORY
            # =================================================

            st.subheader(
                "4. Intelligent Crop Advisory"
            )

            st.write(
                f"**Crop options for {soil_type}:**"
            )

            for crop in crops:

                st.write(
                    f"🌾 {crop}"
                )

            st.caption(
                "Project-defined rule-based recommendation; "
                "not professional agronomic advice."
            )


            # =================================================
            # DATABASE SAVE
            # =================================================

            st.subheader(
                "5. Database Storage"
            )

            if db_password:

                connection = None

                try:

                    connection = create_database_connection(
                        db_password
                    )

                    cursor = connection.cursor()


                    # ------------------------------------------------
                    # SOIL SAMPLE
                    # ------------------------------------------------

                    cursor.execute(
                        """
                        INSERT INTO soil_samples
                        (
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
                        )
                        VALUES
                        (
                            %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s
                        )
                        RETURNING sample_id
                        """,
                        (
                            datetime.now(),
                            soil_type,
                            float(nitrogen),
                            float(phosphorus),
                            float(potassium),
                            float(ph),
                            float(soil_moisture),
                            float(organic_matter),
                            float(temperature),
                            float(humidity),
                            float(rainfall)
                        )
                    )

                    sample_id = cursor.fetchone()[0]


                    # ------------------------------------------------
                    # NUTRIENT PREDICTIONS
                    # ------------------------------------------------

                    cursor.execute(
                        """
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
                        VALUES
                        (
                            %s, %s, %s, %s,
                            %s, %s, %s
                        )
                        """,
                        (
                            sample_id,
                            nitrogen_ml,
                            nitrogen_probability,
                            phosphorus_ml,
                            phosphorus_probability,
                            potassium_ml,
                            potassium_probability
                        )
                    )


                    # ------------------------------------------------
                    # SOIL ASSESSMENT
                    # ------------------------------------------------

                    cursor.execute(
                        """
                        INSERT INTO soil_assessment
                        (
                            sample_id,
                            soil_health_score,
                            soil_health_status,
                            primary_nutrient_concern
                        )
                        VALUES
                        (
                            %s, %s, %s, %s
                        )
                        """,
                        (
                            sample_id,
                            float(health_score),
                            health_status,
                            primary_concern
                        )
                    )


                    # ------------------------------------------------
                    # CROP ADVISORY
                    # ------------------------------------------------

                    for crop in crops:

                        cursor.execute(
                            """
                            INSERT INTO crop_advisory
                            (
                                sample_id,
                                crop_name,
                                recommendation_reason
                            )
                            VALUES
                            (
                                %s, %s, %s
                            )
                            """,
                            (
                                sample_id,
                                crop,
                                f"Suitable project-defined "
                                f"crop option for {soil_type}"
                            )
                        )


                    connection.commit()

                    cursor.close()

                    st.success(
                        "✅ Analysis successfully stored in PostgreSQL."
                    )

                    st.info(
                        f"📌 Sample ID: {sample_id}"
                    )

                except Exception as error:

                    if connection is not None:

                        connection.rollback()

                    st.error(
                        "❌ Database storage failed."
                    )

                    st.code(
                        str(error)
                    )

                finally:

                    if connection is not None:

                        connection.close()

            else:

                st.info(
                    "Enter your PostgreSQL password in the "
                    "sidebar to save this analysis."
                )


        except Exception as error:

            st.error(
                "❌ Soil analysis failed."
            )

            st.code(
                str(error)
            )


# ============================================================
# ANALYSIS HISTORY
# ============================================================

st.divider()

st.header(
    "📋 Analysis History"
)


if db_password:

    history_connection = None

    try:

        history_connection = create_database_connection(
            db_password
        )


        # ========================================================
        # GET ALL SAMPLE IDs
        # ========================================================

        history_df = pd.read_sql_query(
            """
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
            ORDER BY sample_id DESC
            """,
            history_connection
        )


        if history_df.empty:

            st.info(
                "No soil analysis history found."
            )

        else:

            st.write(
                f"Total analyses found: "
                f"**{len(history_df)}**"
            )


            # ====================================================
            # SELECT ID
            # ====================================================

            selected_id = st.selectbox(
                "🔎 Select Sample ID",
                history_df["sample_id"].tolist()
            )


            # ====================================================
            # THIS IS THE IMPORTANT FIX
            # FILTER BY SELECTED ID
            # ====================================================

            selected_sample = history_df[
                history_df["sample_id"] == selected_id
            ]


            if not selected_sample.empty:

                selected_row = selected_sample.iloc[0]


                # ==================================================
                # SAMPLE DETAILS
                # ==================================================

                st.markdown(
                    f"## 📌 Sample ID: {selected_id}"
                )

                st.subheader(
                    "🌱 Soil Sample Details"
                )

                d1, d2, d3 = st.columns(3)


                with d1:

                    st.write(
                        f"**Sample Date:** "
                        f"{selected_row['sample_date']}"
                    )

                    st.write(
                        f"**Soil Type:** "
                        f"{selected_row['soil_type']}"
                    )

                    st.write(
                        f"**Nitrogen (N):** "
                        f"{selected_row['nitrogen']}"
                    )

                    st.write(
                        f"**Phosphorus (P):** "
                        f"{selected_row['phosphorus']}"
                    )


                with d2:

                    st.write(
                        f"**Potassium (K):** "
                        f"{selected_row['potassium']}"
                    )

                    st.write(
                        f"**pH:** "
                        f"{selected_row['ph']}"
                    )

                    st.write(
                        f"**Soil Moisture:** "
                        f"{selected_row['soil_moisture']}"
                    )

                    st.write(
                        f"**Organic Matter:** "
                        f"{selected_row['organic_matter']}"
                    )


                with d3:

                    st.write(
                        f"**Temperature:** "
                        f"{selected_row['temperature']}"
                    )

                    st.write(
                        f"**Humidity:** "
                        f"{selected_row['humidity']}"
                    )

                    st.write(
                        f"**Rainfall:** "
                        f"{selected_row['rainfall']}"
                    )


                # ==================================================
                # NUTRIENT PREDICTION FOR SELECTED ID ONLY
                # ==================================================

                prediction_df = pd.read_sql_query(
                    """
                    SELECT
                        nitrogen_status,
                        nitrogen_probability,
                        phosphorus_status,
                        phosphorus_probability,
                        potassium_status,
                        potassium_probability
                    FROM nutrient_predictions
                    WHERE sample_id = %s
                    """,
                    history_connection,
                    params=(int(selected_id),)
                )


                st.subheader(
                    "🧪 Nutrient ML Predictions"
                )


                if not prediction_df.empty:

                    prediction = prediction_df.iloc[0]

                    p1, p2, p3 = st.columns(3)


                    with p1:

                        st.write(
                            "**Nitrogen:** "
                            + str(
                                prediction[
                                    "nitrogen_status"
                                ]
                            )
                        )

                        st.write(
                            "Probability: "
                            f"{float(prediction['nitrogen_probability']) * 100:.2f}%"
                        )


                    with p2:

                        st.write(
                            "**Phosphorus:** "
                            + str(
                                prediction[
                                    "phosphorus_status"
                                ]
                            )
                        )

                        st.write(
                            "Probability: "
                            f"{float(prediction['phosphorus_probability']) * 100:.2f}%"
                        )


                    with p3:

                        st.write(
                            "**Potassium:** "
                            + str(
                                prediction[
                                    "potassium_status"
                                ]
                            )
                        )

                        st.write(
                            "Probability: "
                            f"{float(prediction['potassium_probability']) * 100:.2f}%"
                        )

                else:

                    st.info(
                        f"No nutrient prediction found for "
                        f"Sample ID {selected_id}."
                    )


                # ==================================================
                # ASSESSMENT FOR SELECTED ID ONLY
                # ==================================================

                assessment_df = pd.read_sql_query(
                    """
                    SELECT
                        soil_health_score,
                        soil_health_status,
                        primary_nutrient_concern
                    FROM soil_assessment
                    WHERE sample_id = %s
                    """,
                    history_connection,
                    params=(int(selected_id),)
                )


                st.subheader(
                    "❤️ Hybrid Soil Assessment"
                )


                if not assessment_df.empty:

                    assessment = assessment_df.iloc[0]

                    a1, a2, a3 = st.columns(3)


                    with a1:

                        st.metric(
                            "Health Score",
                            f"{assessment['soil_health_score']}/100"
                        )


                    with a2:

                        st.metric(
                            "Health Status",
                            assessment[
                                "soil_health_status"
                            ]
                        )


                    with a3:

                        st.metric(
                            "Primary Concern",
                            assessment[
                                "primary_nutrient_concern"
                            ]
                        )

                else:

                    st.info(
                        f"No assessment found for "
                        f"Sample ID {selected_id}."
                    )


                # ==================================================
                # ADVISORY FOR SELECTED ID ONLY
                # ==================================================

                advisory_df = pd.read_sql_query(
                    """
                    SELECT
                        crop_name,
                        recommendation_reason
                    FROM crop_advisory
                    WHERE sample_id = %s
                    """,
                    history_connection,
                    params=(int(selected_id),)
                )


                st.subheader(
                    "🌾 Crop Advisory"
                )


                if not advisory_df.empty:

                    for _, advisory in advisory_df.iterrows():

                        st.write(
                            f"🌾 **{advisory['crop_name']}**"
                        )

                        st.caption(
                            advisory[
                                "recommendation_reason"
                            ]
                        )

                else:

                    st.info(
                        f"No crop advisory found for "
                        f"Sample ID {selected_id}."
                    )


    except Exception as error:

        st.error(
            "❌ Could not load Analysis History."
        )

        st.code(
            str(error)
        )

    finally:

        if history_connection is not None:

            history_connection.close()

else:

    st.info(
        "🔐 Enter your PostgreSQL password in the sidebar "
        "to view Analysis History."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI-Powered Soil Analytics System | "
    "ResNet-50 + Gradient Boosting + "
    "Hybrid Assessment + PostgreSQL"
)