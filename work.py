from langchain_ollama import ChatOllama
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader
)
from langchain.prompts import PromptTemplate

llm = ChatOllama(
    model="deepseek-v3.1:671b-cloud",
    temperature=0.9
)

def load_resume(uploaded_file):
    try:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if file_extension == 'pdf':
            loader = PyPDFLoader(uploaded_file.name)
        elif file_extension == 'docx':
            loader = Docx2txtLoader(uploaded_file.name)
        elif file_extension == 'txt':
            loader = TextLoader(uploaded_file.name)
        else:
            return None 

        docs = loader.load()
        
        import os
        os.remove(uploaded_file.name)
        
        return docs
    except Exception as e:
        print(f"Error loading file: {e}")
        return None



PROMPT_TEMPLATE = """
You are an expert HR data extraction system. Your task is to accurately parse the provided resume text and convert it into a structured JSON object.

Follow these rules strictly:
1.  **Output Format:** The output must be a single, valid JSON object. Do not include any text, explanations, or markdown formatting before or after the JSON.
2.  **Schema:** Adhere exactly to the JSON schema provided below.
3.  **Missing Information:** If a specific piece of information is not found in the resume, use `null` as the value for that field. For lists like work experience or skills, use an empty array `[]` if none are found.
4.  **Extraction, Not Invention:** Extract information directly as it is written. Do not infer or invent data that is not present.

**JSON Schema:**
{{
  "contact_info": {{
    "name": "string",
    "email": "string",
    "phone": "string",
    "location": "string",
    "linkedin_url": "string"
  }},
  "summary": "string",
  "work_experience": [
    {{
      "job_title": "string",
      "company": "string",
      "start_date": "string",
      "end_date": "string",
      "responsibilities": [
        "string"
      ]
    }}
  ],
  "education": [
    {{
      "degree": "string",
      "institution": "string",
      "graduation_date": "string"
    }}
  ],
  "skills": [
    "string"
  ]
}}

**Resume Text to Parse:**
---
{text}
---
"""

prompt = PromptTemplate(template=PROMPT_TEMPLATE,input_variables=['text'])

