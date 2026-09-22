import math


def parameter_score(value, minimum, maximum):
    """
    Calculate a score from 0 to 100.

    100 = value is within the preferred range.
    Values outside the range receive a lower score.
    """

    if minimum <= value <= maximum:
        return 100.0

    if value < minimum:
        distance = minimum - value
    else:
        distance = value - maximum

    range_size = maximum - minimum

    if range_size == 0:
        return 0.0

    score = 100 - (distance / range_size) * 100

    return max(0.0, score)


def calculate_soil_health(soil):
    """
    Calculate individual soil-health indicator scores
    and an overall soil-health score.
    """

    scores = {}

    # Preferred prototype ranges
    scores["nitrogen"] = parameter_score(
        soil["n"], 20, 50
    )

    scores["phosphorus"] = parameter_score(
        soil["p"], 10, 40
    )

    scores["potassium"] = parameter_score(
        soil["k"], 100, 300
    )

    scores["ph"] = parameter_score(
        soil["ph"], 6.0, 7.5
    )

    scores["moisture"] = parameter_score(
        soil["moisture"], 30, 70
    )

    scores["organic_matter"] = parameter_score(
        soil["organic_matter"], 2, 5
    )

    # Equal weighting for the prototype
    overall_score = sum(scores.values()) / len(scores)

    overall_score = round(overall_score, 2)

    return scores, overall_score


def classify_health(score):

    if score >= 80:
        return "Healthy"

    elif score >= 60:
        return "Moderately Healthy"

    elif score >= 40:
        return "Needs Improvement"

    else:
        return "Poor"


def analyze_soil_health(soil):

    scores, overall_score = calculate_soil_health(soil)

    health_status = classify_health(
        overall_score
    )

    return scores, overall_score, health_status


def main():

    print("=" * 70)
    print("SOIL HEALTH ANALYSIS")
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

    scores, overall_score, health_status = analyze_soil_health(
        soil
    )

    print("\nSOIL HEALTH INDICATORS")
    print("----------------------")

    for parameter, score in scores.items():

        print(
            f"{parameter.replace('_', ' ').title():20}: "
            f"{score:.2f}/100"
        )

    print("\nOVERALL SOIL HEALTH")
    print("-------------------")

    print(f"Health Score : {overall_score}/100")
    print(f"Status       : {health_status}")

    print("\n" + "=" * 70)
    print("Soil health analysis completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()