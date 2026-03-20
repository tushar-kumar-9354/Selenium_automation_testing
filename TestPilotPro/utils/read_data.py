import csv

def get_login_data():
    rows = []

    with open("data/login_data.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append((row["username"], row["password"]))

    return rows