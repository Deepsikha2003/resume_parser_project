import requests
import os
import json

# The URL for your Flask server's API endpoint
url = "http://127.0.0.1:5000/parse"

# The file you want to send (make sure this file exists in your data/raw_resumes folder)
file_path = os.path.join("data", "raw_resumes", "resume1.pdf") 

try:
    # Open the file in binary mode
    with open(file_path, "rb") as f:
        # Prepare the file to be sent in the POST request
        files = {"file": f}

        print(f"Sending file: {file_path}")

        # Send the POST request to the server
        response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response in a readable format
        print("\nSuccessfully parsed resume:")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"\nError: Server returned status code {response.status_code}")
        print(response.text)

except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")