# Resume Analyzer

The Resume Analyzer is a web application that analyzes resumes against job descriptions to provide insights on matching skills, missing skills, and overall relevance.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package installer)
- Django
- A virtual environment tool (optional but recommended)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd resume_analyzer_project
   ```

2. **Create a virtual environment (optional):**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your `TOGETHER_API_KEY`:

   ```plaintext
   TOGETHER_API_KEY=your_api_key_here
   ```

## Running the Application

1. **Apply migrations:**

   ```bash
   cd resume_analyzer_project
   python manage.py migrate
   ```

2. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

3. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/` to access the Resume Screening System.

## Usage

- Enter the job description in the provided text area.
- Upload a resume in PDF format.
- Click the "Analyze" button to get the analysis results.

