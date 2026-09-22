import csv
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CROP_FILE = os.path.join(
    BASE_DIR,
    "Crop_Suitability",
    "crop_soil_compatibility.csv"
)


def load_crop_data(file_path):
    crops = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            crop = {
                "crop": row["crop"],
                "min_n": float(row["min_n"]),
                "max_n": float(row["max_n"]),
                "min_p": float(row["min_p"]),
                "max_p": float(row["max_p"]),
                "min_k": float(row["min_k"]),
                "max_k": float(row["max_k"]),
                "min_ph": float(row["min_ph"]),
                "max_ph": float(row["max_ph"]),
                "min_moisture": float(row["min_moisture"]),
                "max_moisture": float(row["max_moisture"]),
                "min_organic_matter": float(row["min_organic_matter"]),
                "max_organic_matter": float(row["max_organic_matter"])
            }

            crops.append(crop)

    return crops


def parameter_score(value, minimum, maximum):
    """
    Returns a score from 0 to 100.

    100 = value is inside the preferred range.
    Outside the range = lower score based on distance.
    """

    if minimum <= value <= maximum:
        return 100.0

    if value < minimum:
        distance = minimum - value
        range_size = maximum - minimum
    else:
        distance = value - maximum
        range_size = maximum - minimum

    if range_size == 0:
        return 0.0

    score = 100 - (distance / range_size) * 100

    return max(0.0, score)


def calculate_crop_score(soil, crop):
    scores = []

    scores.append(
        parameter_score(
            soil["n"],
            crop["min_n"],
            crop["max_n"]
        )
    )

    scores.append(
        parameter_score(
            soil["p"],
            crop["min_p"],
            crop["max_p"]
        )
    )

    scores.append(
        parameter_score(
            soil["k"],
            crop["min_k"],
            crop["max_k"]
        )
    )

    scores.append(
        parameter_score(
            soil["ph"],
            crop["min_ph"],
            crop["max_ph"]
        )
    )

    scores.append(
        parameter_score(
            soil["moisture"],
            crop["min_moisture"],
            crop["max_moisture"]
        )
    )

    scores.append(
        parameter_score(
            soil["organic_matter"],
            crop["min_organic_matter"],
            crop["max_organic_matter"]
        )
    )

    overall_score = sum(scores) / len(scores)

    return round(overall_score, 2)


def classify_suitability(score):

    if score >= 80:
        return "Highly Suitable"

    elif score >= 60:
        return "Suitable"

    elif score >= 40:
        return "Moderately Suitable"

    else:
        return "Less Suitable"


def recommend_crops(soil):

    crops = load_crop_data(CROP_FILE)

    results = []

    for crop in crops:

        score = calculate_crop_score(
            soil,
            crop
        )

        suitability = classify_suitability(
            score
        )

        results.append({
            "crop": crop["crop"],
            "score": score,
            "suitability": suitability
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


def main():

    print("=" * 70)
    print("CROP SUITABILITY ANALYSIS")
    print("=" * 70)

    soil = {
        "n": 35,
        "p": 25,
        "k": 180,
        "ph": 6.8,
        "moisture": 50,
        "organic_matter": 3.0
    }

    print("\nINPUT SOIL PARAMETERS")
    print("---------------------")

    print(f"Nitrogen            : {soil['n']}")
    print(f"Phosphorus          : {soil['p']}")
    print(f"Potassium           : {soil['k']}")
    print(f"pH                  : {soil['ph']}")
    print(f"Moisture            : {soil['moisture']}")
    print(f"Organic Matter      : {soil['organic_matter']}")

    results = recommend_crops(soil)

    print("\nCROP SUITABILITY RESULTS")
    print("------------------------")

    for index, result in enumerate(results, start=1):

        print(
            f"{index}. {result['crop']:12} "
            f"Score: {result['score']:6.2f} "
            f"Status: {result['suitability']}"
        )

    print("\n" + "=" * 70)
    print("Crop suitability analysis completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()