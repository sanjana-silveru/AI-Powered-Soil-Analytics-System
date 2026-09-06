import os

for dataset in ["Cleaned_Dataset", "Resized_Dataset"]:

    total = 0

    print("\n", dataset)

    for class_name in os.listdir(dataset):
        class_path = os.path.join(dataset, class_name)

        if os.path.isdir(class_path):
            count = 0

            for filename in os.listdir(class_path):
                if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                    count += 1

            print(class_name, ":", count)
            total += count

    print("TOTAL:", total)