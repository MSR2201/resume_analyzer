import os
from dotenv import load_dotenv
from langchain_together import ChatTogether
import PyPDF2
from typing import Dict, Tuple
import json

# Load environment variables
load_dotenv()
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')

class ResumeAnalyzer:
    def __init__(self):
        self.chat = ChatTogether(
            together_api_key=TOGETHER_API_KEY,
            model="meta-llama/Llama-3-70b-chat-hf",
        )

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text content from a PDF file."""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")

    def analyze_documents(self, resume_path: str, job_description: str) -> str:
        """Analyze resume and job description."""
        resume_text = self.extract_text_from_pdf(resume_path)
        
        prompt = f"""
        Please analyze the following resume and job description. Provide a concise analysis with:
        1. Top 5 key skills found in the job description
        2. Top 5 matching skills found in the resume
        3. A relevance score (0-100) comparing the resume to the job requirements
        4. A brief explanation (2-3 sentences) of the score
        
        Keep the response brief and well-structured.
        
        Job Description:
        {job_description}

        Resume:
        {resume_text}
        """

        response = self.chat.invoke(prompt)
        return response.content

def main():
    # Example usage
    analyzer = ResumeAnalyzer()
    
    # Get inputs from user
    resume_path =  "C:/Users/sanke/Desktop/Resume/Moreddy_Sankeerth_Reddy.pdf"
    job_description = "We are looking for a talented Prompt Engineer to join our team and play a crucial role in enhancing our AI-driven content generation platform. Your expertise in prompt engineering will help us optimize AI interactions, improve content quality, and maximize engagement for businesses using our platform. If you are passionate about LLMs, NLP, and AI-driven solutions, this is an opportunity to work on cutting-edge technology and make a real impact. Required Qualifications Bachelor’s degree in Computer Science, Linguistics, or a related field. 2+ years of experience in AI, machine learning, or related areas. Proficiency in programming languages such as Python or JavaScript. Experience in natural language processing (NLP) techniques. Strong understanding of AI model behavior and limitations. Exceptional communication and collaboration skills. Ability to analyze data and derive actionable insights. Experience with UX/UI design principles is a plus. Familiarity with version control systems like Git. Knowledge of prompt testing tools and methodologies. Creative mindset with a focus on problem-solving. Adaptability to changing technologies and processes. Experience working in Agile development environments. Understanding of user-centered design principles. Strong organizational skills with attention to detail."
    
    try:
        results = analyzer.analyze_documents(resume_path, job_description)
        print("\n=== Analysis Results ===")
        print(results)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
