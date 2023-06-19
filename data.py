import csv
import random
from datetime import datetime, timedelta

# Set the start time as the current time
start_time = datetime.now()

# Open the CSV file in write mode
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Timestamp", "Percent Full"])

    # Loop over the range 10,000,000 times
    for i in range(10_000_000):
        # Create a timestamp that is 'i' seconds after the start time
        timestamp = start_time + timedelta(seconds=i)

        # Generate a random "percent full" value
        percent_full = random.uniform(0, 100)

        # Write the row to the CSV file
        writer.writerow([timestamp.isoformat(), percent_full])
