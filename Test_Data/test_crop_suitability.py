import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "Crop_Suitability"
    )
)

from crop_suitability import recommend_crops


test_cases = [
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
        "name": "Acidic Low-Nutrient Soil",
        "n": 12,
        "p": 8,
        "k": 70,
        "ph": 5.0,
        "moisture": 30,
        "organic_matter": 1.0
    },
    {
        "name": "Alkaline High-Nutrient Soil",
        "n": 65,
        "p": 45,
        "k": 320,
        "ph": 8.2,
        "moisture": 75,
        "organic_matter": 5.5
    }
]


print("=" * 70)
print("CROP SUITABILITY TESTING")
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

    results = recommend_crops(soil)

    print("\nTop 5 Suitable Crops:")

    for index, result in enumerate(results[:5], start=1):

        print(
            f"{index}. {result['crop']:12} "
            f"Score: {result['score']:6.2f} "
            f"Status: {result['suitability']}"
        )


print("\n" + "=" * 70)
print("ALL CROP SUITABILITY TEST CASES COMPLETED SUCCESSFULLY")
print("=" * 70)