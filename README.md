Resume Parser Web Application
📝 Overview
This is a web application that automatically extracts key information from resume files (PDF and DOCX). The application uses a Python backend built with Flask and natural language processing (spaCy) to identify a candidate's name, contact information, skills, and education. The front-end is a simple HTML/JavaScript interface that allows users to upload a file and view the parsed data.

This project is useful for recruiters and HR professionals who need a quick and efficient way to process multiple resumes without manually reading through each one.

🚀 Features
File Upload: Supports uploading resume files in both .pdf and .docx formats.

Data Extraction: Accurately extracts a candidate's name, email, and phone number.

Skills Identification: Scans the resume for a predefined list of technical skills.

Education Recognition: Identifies educational institutions using spaCy's Named Entity Recognition (NER).

Web Interface: A simple, user-friendly front-end for seamless file uploads and data display.

🛠️ Installation
To get a local copy up and running, follow these steps.

Prerequisites
Python 3.8 or higher

pip (Python package installer)

Setup
Clone the repository:

Bash

git clone https://github.com/your-username/resume-parser-project.git
cd resume-parser-project
Create and activate a virtual environment:

Bash

python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
Install the required libraries:

Bash

pip install -r requirements.txt
Download the spaCy model:
This command is included in your parser.py file, but you can also run it manually to ensure the model is installed.

Bash

python -m spacy download en_core_web_sm
🖥️ Usage
To run the web application, you must start the Flask server and then access it from your browser.

Start the Flask server:
From the project's root directory, run the following command. The server will start on http://127.0.0.1:5000.

Bash

python src/app.py
Access the web app:
Open your web browser and go to http://127.0.0.1:5000/. You will see the web interface for uploading a resume.

Upload a file:
Click "Choose File," select a .pdf or .docx resume, and then click "Analyze Resume" to see the extracted information.

📂 Project Structure
resume_parser_project/
├── .venv/                   # Virtual environment
├── data/
│   └── raw_resumes/         # Sample resumes
├── src/
│   ├── templates/
│   │   └── index.html       # Front-end HTML
│   ├── app.py               # Flask server code
│   └── parser.py            # Resume parsing logic
└── requirements.txt         # Project dependencies
🤝 Contributing
Contributions are welcome! If you have any suggestions or find a bug, please feel free to open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License.


