import csv
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

KNOWLEDGE_BASE = os.path.join(
    BASE_DIR,
    "Knowledge_Base",
    "agricultural_knowledge_base.csv"
)

RULES_FILE = os.path.join(
    BASE_DIR,
    "Knowledge_Base",
    "recommendation_rules.csv"
)


def load_csv_file(file_path):
    data = {}

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            parameter = row["parameter"]
            condition = row["condition"]

            if parameter not in data:
                data[parameter] = {}

            data[parameter][condition] = row

    return data


def classify_soil(n, p, k, ph, moisture, organic_matter):

    conditions = {}

    conditions["nitrogen"] = (
        "low" if n < 20
        else "high" if n > 50
        else "adequate"
    )

    conditions["phosphorus"] = (
        "low" if p < 10
        else "high" if p > 40
        else "adequate"
    )

    conditions["potassium"] = (
        "low" if k < 100
        else "high" if k > 300
        else "adequate"
    )

    conditions["ph"] = (
        "acidic" if ph < 6
        else "alkaline" if ph > 7.5
        else "suitable"
    )

    conditions["moisture"] = (
        "low" if moisture < 30
        else "high" if moisture > 70
        else "suitable"
    )

    conditions["organic_matter"] = (
        "low" if organic_matter < 2
        else "high" if organic_matter > 5
        else "adequate"
    )

    return conditions


def generate_recommendations(conditions, rules):

    recommendations = []

    for parameter, condition in conditions.items():

        if parameter in rules:

            rule = rules[parameter].get(condition)

            if rule:

                recommendations.append({
                    "parameter": parameter,
                    "condition": condition,
                    "action": rule["action"],
                    "guidance": rule["guidance"]
                })

    return recommendations


def analyze_soil(n, p, k, ph, moisture, organic_matter):

    rules = load_csv_file(RULES_FILE)

    conditions = classify_soil(
        n,
        p,
        k,
        ph,
        moisture,
        organic_matter
    )

    recommendations = generate_recommendations(
        conditions,
        rules
    )

    return conditions, recommendations


def main():

    print("=" * 65)
    print("AI-POWERED SOIL RECOMMENDATION ENGINE")
    print("=" * 65)

    soil = {
        "nitrogen": 15,
        "phosphorus": 25,
        "potassium": 120,
        "ph": 5.5,
        "moisture": 45,
        "organic_matter": 1.5
    }

    print("\nINPUT SOIL PARAMETERS")
    print("---------------------")

    for key, value in soil.items():
        print(f"{key.replace('_', ' ').title():20}: {value}")

    conditions, recommendations = analyze_soil(
        soil["nitrogen"],
        soil["phosphorus"],
        soil["potassium"],
        soil["ph"],
        soil["moisture"],
        soil["organic_matter"]
    )

    print("\nSOIL CONDITIONS")
    print("----------------")

    for parameter, condition in conditions.items():
        print(
            f"{parameter.replace('_', ' ').title():20}: "
            f"{condition}"
        )

    print("\nRECOMMENDATIONS")
    print("----------------")

    for item in recommendations:

        print(f"\n{item['parameter'].upper()}")
        print(f"Condition : {item['condition']}")
        print(f"Action    : {item['action']}")
        print(f"Guidance  : {item['guidance']}")

    print("\n" + "=" * 65)
    print("Recommendation engine completed successfully.")
    print("=" * 65)


if __name__ == "__main__":
    main()