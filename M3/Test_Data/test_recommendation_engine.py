import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "Recommendation_Engine"
    )
)

from recommendation_engine import analyze_soil


test_cases = [

    {
        "name": "Low Nutrient Soil",
        "n": 10,
        "p": 5,
        "k": 70,
        "ph": 5.2,
        "moisture": 25,
        "organic_matter": 1.0
    },

    {
        "name": "Balanced Soil",
        "n": 35,
        "p": 25,
        "k": 180,
        "ph": 6.8,
        "moisture": 50,
        "organic_matter": 3.0
    },

    {
        "name": "High Nutrient Soil",
        "n": 70,
        "p": 50,
        "k": 350,
        "ph": 8.0,
        "moisture": 80,
        "organic_matter": 6.0
    }
]


print("=" * 70)
print("RECOMMENDATION ENGINE TESTING")
print("=" * 70)


for test in test_cases:

    print(f"\nTEST CASE: {test['name']}")
    print("-" * 50)

    conditions, recommendations = analyze_soil(
        test["n"],
        test["p"],
        test["k"],
        test["ph"],
        test["moisture"],
        test["organic_matter"]
    )

    print("\nConditions:")

    for parameter, condition in conditions.items():
        print(
            f"{parameter.replace('_', ' ').title():20}: "
            f"{condition}"
        )

    print("\nRecommendations:")

    for item in recommendations:
        print(
            f"- {item['parameter'].title()}: "
            f"{item['action']}"
        )


print("\n" + "=" * 70)
print("ALL TEST CASES COMPLETED SUCCESSFULLY")
print("=" * 70)