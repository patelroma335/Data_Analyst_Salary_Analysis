import csv
from datetime import datetime, timedelta

# convert data string from 30 days, today, now to a valid string date
def main():
    # read from a csv then write to a new csv
    with open("job_new.csv") as f1, open("job_new_2.csv", "w") as f2:
        reader = csv.reader(f1)
        writer = csv.writer(f2)
        for row in reader:
            if row[0] == "job_Title":
                # Get rid of last three columns
                row = row[:-3]
                row.append("formatted_date")
                writer.writerow(row)
                continue

            # Get the date column, and convert to new date format
            date_str = row[-3]
            formatted_date = convert_date(date_str)

            # Get rid of the last three columns, and append new date
            row = row[:-3]
            row.append(formatted_date)
            writer.writerow(row)


def convert_date(date_str):
    now = datetime.now()
    if date_str == "Just" or date_str == "Today":
        return f"{now.year}/{now.month}/{now.day}"

    if date_str == "30+":
        dt = now - timedelta(31)
        return f"{dt.year}/{dt.month}/{dt.day}"

    dt = now - timedelta(int(date_str))
    return f"{dt.year}/{dt.month}/{dt.day}"


if __name__ == "__main__":
    main()
