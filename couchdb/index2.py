import csv
import json
import requests

# Function to enable Admin Party mode
def enable_admin_party_mode(couchdb_url):
    config_url = couchdb_url + "/_config/couch_httpd_auth/disable_httpd_authentication"
    response = requests.put(config_url, data='true')
    if response.status_code == 200:
        print("Admin Party mode enabled successfully.")
    else:
        print("Failed to enable Admin Party mode:", response.text)

# Function to upload data to CouchDB in batches
def upload_data_to_couchdb(data, db_url, batch_size=100000):
    batched_data = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    for batch in batched_data:
        docs = {"docs": batch}
        response = requests.post(db_url + "/_bulk_docs", json=docs)
        if response.status_code != 201:
            print("Error uploading batch:", response.text)

# Function to read data from CSV file
def read_csv(csv_file):
    data = []
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Main function
def main():
    # CouchDB settings
    couchdb_url = "http://localhost:5984"  # Change this to your CouchDB server URL
    db_url = couchdb_url + "/user"  # Change this to your CouchDB database URL
    csv_file = "user.csv"  # Change this to your CSV file path

    # Enable Admin Party mode
    enable_admin_party_mode(couchdb_url)

    # Read data from CSV file
    data = read_csv(csv_file)

    # Upload data to CouchDB
    upload_data_to_couchdb(data, db_url)

if __name__ == "__main__":
    main()
