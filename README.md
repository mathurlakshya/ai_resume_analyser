# AI Resume Analyzer

A small Streamlit application that uses Google's Gemini API to review a resume PDF and provide structured career feedback.

The project explores a practical AI workflow: upload a document, extract its text, send the extracted content to a generative AI model, display the response, and create a downloadable PDF report.

> **Project status:** Learning project / work in progress. The feedback is AI-generated and should be reviewed by the user. It is not a validated ATS score, hiring assessment, or guarantee of employment outcomes.

## Features

- Upload a resume in PDF format.
- Extract readable text from the uploaded PDF using PyPDF2.
- Request AI-generated feedback using Google's Gemini API.
- Display feedback covering:
  - Resume score (as estimated by the model)
  - Potentially missing skills
  - Strengths and weaknesses
  - Suggested improvements
  - Potentially suitable career roles
  - ATS-friendliness observations
- Generate and download a PDF containing the AI analysis.

## Tech stack

- **Python**
- **Streamlit** — interactive web application
- **PyPDF2** — PDF text extraction
- **Google Generative AI SDK** — Gemini model integration
- **ReportLab** — PDF report generation

## How the application works

1. The user uploads a PDF resume through the Streamlit interface.
2. PyPDF2 extracts text from the PDF pages.
3. The extracted text is included in a prompt requesting structured resume feedback.
4. When the user selects **Analyze Resume**, the configured Gemini model generates a response.
5. The response is displayed in the app and can be downloaded as a PDF report.

## Getting started

### Prerequisites

- Python 3.9 or newer.
- A Google Gemini API key.
- Internet access to install dependencies and call the Gemini API.

### 1. Clone the repository

```bash
git clone https://github.com/mathurlakshya/ai_resume_analyser.git
cd ai_resume_analyser
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a file at `.streamlit/secrets.toml` with the following content:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
```

Do not commit this file or share your API key. If a real key has ever been committed to a public repository, revoke or rotate it in the provider dashboard and replace it with a new key. Keep secrets in your local environment or a secure deployment secrets manager.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will print a local address in the terminal. Open that address in your browser.

## Example use

1. Open the app.
2. Upload a text-based PDF resume.
3. Review the extracted text.
4. Select **Analyze Resume**.
5. Read the generated feedback and download the PDF report if desired.

Scanned PDFs may not produce useful extracted text because this version uses text extraction rather than optical character recognition (OCR).

## Privacy and responsible use

Resumes can contain personal information such as phone numbers, email addresses, education history and employment details.

- Only upload documents you have permission to process.
- The extracted resume text is sent to Google's Gemini API when analysis is requested. Review Google's current data and privacy terms before using the service with sensitive information.
- Avoid uploading another person's resume without their permission.
- Review AI-generated suggestions for accuracy and relevance. Do not treat the generated score or ATS comments as an authoritative hiring decision.
- Do not commit API keys, uploaded resumes, or generated reports to a public repository.

## Current limitations and possible improvements

This is an early project, so there are several areas that could be improved:

- Add OCR support for scanned/image-based PDFs.
- Improve input validation and user-friendly error handling for unreadable or empty PDFs.
- Escape extracted resume text before inserting it into ReportLab Paragraph markup.
- Add configurable analysis prompts and role-specific feedback.
- Make report generation use a temporary file or in-memory buffer rather than a fixed filename.
- Add tests for PDF extraction, prompt construction and report generation.
- Improve secret management and deployment configuration.

## Learning outcomes

Building this project is a way to practise connecting a Python web interface with document parsing, a generative AI API, prompt design and PDF generation. It also highlights important considerations around privacy, API credentials and evaluating AI-generated feedback.

Feedback and suggestions are welcome.

## License

No license has been added to this repository yet. Until a license is included, all rights remain with the repository owner; please ask before reusing or distributing the code.
