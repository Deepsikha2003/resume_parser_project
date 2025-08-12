import requests
import os

# This is the URL for your server's resume parsing endpoint
url = "http://127.0.0.1:5000/parse"

# Specify the path to a resume file in your project's data folder
file_path = os.path.join("data", "raw_resumes", "resume1.pdf") # You can change "resume1.pdf" to "resume2.docx"

# Send the POST request with the file
try:
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)

    # Print the JSON response from the server
    print(response.json())
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")