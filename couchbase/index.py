import csv
from faker import Faker
import random

# Initialize Faker for generating random names
fake = Faker()

# Number of data points to generate
num_data_points = 100000

# File name for the CSV file
csv_file_name = "user.csv"

# Write data to CSV file
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["name", "price"])
    
    # Write data rows
    for _ in range(num_data_points):
        name = fake.name()  # Generate random name
        price = round(random.uniform(1.0, 1000.0), 2)  # Generate random price between 1 and 1000 with 2 decimal places
        writer.writerow([name, price])

print(f"CSV file '{csv_file_name}' with {num_data_points} data points created successfully.")
