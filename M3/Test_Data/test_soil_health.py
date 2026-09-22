import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "Soil_Health"
    )
)

from soil_health import analyze_soil_health


test_cases = [
    {
        "name": "Healthy Soil",
        "n": 35,
        "p": 25,
        "k": 180,
        "ph": 6.8,
        "moisture": 50,
        "organic_matter": 3.0
    },
    {
        "name": "Soil Needing Improvement",
        "n": 15,
        "p": 8,
        "k": 80,
        "ph": 5.2,
        "moisture": 25,
        "organic_matter": 1.0
    },
    {
        "name": "High Nutrient / Alkaline Soil",
        "n": 65,
        "p": 45,
        "k": 350,
        "ph": 8.2,
        "moisture": 80,
        "organic_matter": 6.0
    }
]


print("=" * 70)
print("SOIL HEALTH SCORING TESTING")
print("=" * 70)


for test in test_cases:

    print(f"\nTEST CASE: {test['name']}")
    print("-" * 55)

    soil = {
        "n": test["n"],
        "p": test["p"],
        "k": test["k"],
        "ph": test["ph"],
        "moisture": test["moisture"],
        "organic_matter": test["organic_matter"]
    }

    scores, overall_score, health_status = analyze_soil_health(
        soil
    )

    print("\nIndicator Scores:")

    for parameter, score in scores.items():

        print(
            f"{parameter.replace('_', ' ').title():20}: "
            f"{score:.2f}/100"
        )

    print("\nOverall Soil Health:")
    print(f"Score  : {overall_score}/100")
    print(f"Status : {health_status}")


print("\n" + "=" * 70)
print("ALL SOIL HEALTH TEST CASES COMPLETED SUCCESSFULLY")
print("=" * 70)