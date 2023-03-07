import json
import csv
from argparse import ArgumentParser


def load_json(json_path: str) -> dict:
    with open(json_path) as f:
        return json.load(f)


def create_array_of_arrays(recommendations):
    csv_header = [["Drug", "Source", "Recommendation", "Strength", "Guideline", "Factors"]]
    for drugname, sources in recommendations.items():
        for source, data in sources.items():
            if data == []:
                continue
            for item in data:
                strength = ""
                if "strength" in item:
                    strength = item["strength"]
                drugline = [drugname, source, item["recommendation"], strength, item["guideline"], item["factors"]]
                csv_header.append(drugline)
    return csv_header


def save_to_csv(array: list):
    file_path = "recommendations.csv"
    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in array:
            csv_writer.writerow(row)

def main():
    parser = ArgumentParser()
    parser.add_argument("-r", "--openpgx_json")
    args = vars(parser.parse_args())

    recommendations = load_json(args["openpgx_json"])
    data = create_array_of_arrays(recommendations)
    save_to_csv(data)


if __name__ == "__main__":
    main()
