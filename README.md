📄 AI-Powered Resume Parser
An intelligent web application that transforms unstructured resume documents into clean, structured JSON data using the power of Large Language Models.
Overview
In the world of recruitment, manually sifting through hundreds of resumes is a time-consuming, repetitive, and often biased process. This project offers a modern solution by leveraging AI to automate the initial screening stages.

This AI-Powered Resume Parser is a simple web app built with Python and Streamlit that allows anyone to upload a resume in PDF, DOCX, or TXT format. Behind the scenes, it uses a powerful Large Language Model (like DeepSeek or Llama3 via Ollama) to instantly read the document, understand its context, and extract key information like contact details, work experience, and skills.

The best part? It transforms the unstructured text into clean, structured JSON data, turning a pile of documents into a usable and organized talent profile. This is a game-changer for automating recruitment and making the hiring process faster and more efficient.

Features
Multi-Format Support: Upload resumes in .pdf, .docx, and .txt formats.

AI-Powered Extraction: Utilizes a local LLM via Ollama to intelligently parse resume content.

Structured JSON Output: Converts messy resume text into a clean, predictable JSON format.

Instant Preview: Shows the raw text extracted from the document before parsing.

Downloadable Results: Download the structured JSON data as a .json file for easy integration with other systems.

User-Friendly Interface: A simple and intuitive UI built with Streamlit.

Tech Stack
Backend & Logic: Python

Web Framework: Streamlit

AI/LLM Orchestration: LangChain

LLM Hosting: Ollama (for running models like DeepSeek, Llama3, etc., locally)

Document Loaders: PyPDFLoader, Docx2txtLoader, TextLoader

Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the Repository

git clone https://github.com/Krishna-devk/Resume-Parser.git

cd Resume-Parser

2. Create a Virtual Environment (Recommended)

# For Windows
python -m venv .venv

.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

4. Set up Ollama

Download and install Ollama for your operating system.

Pull the model you want to use from the command line. For example:

ollama pull deepseek-v3.1:671b-cloud

Ensure the Ollama application is running in the background.

How to Run
Once the setup is complete, you can launch the Streamlit application with a single command:

streamlit run ui.py

Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

How It Works
File Upload: The user uploads a resume file through the Streamlit interface.

Text Extraction: A suitable LangChain DocumentLoader reads the file and extracts all the text content.

Prompt Engineering: The extracted text is inserted into a carefully designed prompt template that instructs the LLM on how to behave and what JSON schema to follow.

LLM Invocation: The complete prompt is sent to the locally running LLM via Ollama.

JSON Generation: The LLM processes the text and returns a structured JSON string.

Display & Download: The application displays the formatted JSON and provides a button to download the result as a .json file.

Future Improvements
[ ] Batch Processing: Allow users to upload multiple resumes at once.

[ ] Database Integration: Save the parsed JSON data to a database (like SQLite or Firestore) to create a searchable talent pool.

[ ] Advanced Analytics: Build a dashboard to visualize skills, experience levels, and other trends from the parsed resumes.

[ ] Dockerize Application: Package the application into a Docker container for easy deployment.

Feel free to contribute to this project by submitting a pull request or opening an issue!
