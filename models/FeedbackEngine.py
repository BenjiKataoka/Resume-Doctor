from typing import Any
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_core.messages import SystemMessage, HumanMessage
import json

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from models import PDFProcessor

class FeedBack:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.7,
            model="gpt-4o",
            openai_api_key = os.getenv("OPENAI_API_KEY")
        )

    @staticmethod
    def generateFeedback(self, resume: str) -> dict:
        #    def generateFeedback(self, analysis: dict, resume: str, jobdesc: str) -> str:
        prompt = ("""
        You are an expert tech recruiter reviewing resumes for a software engineer role and your client is in dire need of your help!"
                      "Given this resume: { resume },":

        - A "score" out of 10 indicating the resume's strength.
        - A list of specific "strengths".
        - A list of actionable "suggestions" for improvement as well as constructive criticism.

        Example:
        {
        "score": 8.7,
        "strengths": [
        "Strong and relevant work experience in software engineering and R&D roles",
        "Excellent academic background with high GPA and relevant coursework",
        "Robust technical skills across languages, frameworks, and tools",
        "Impressive projects demonstrating practical knowledge and initiative",
        "Clear and well-organized layout with strong action verbs"
      ],
          "suggestions": [
            "Add a brief 2–3 sentence professional summary at the top to highlight your core strengths and goals",
            "In projects, briefly explain your personal contribution and the project impact or outcomes",
            "Include metrics for project achievements if applicable (e.g., number of users, performance improvements)",
            "Use consistent formatting in bullet points (some lines break mid-sentence unnecessarily)",
            "Consider grouping technologies/tools under categories (e.g., Databases, Dev Tools) for quick scanning"
          ],
      "constructive_criticism": [
        "Your experience is solid, but a recruiter may not immediately understand the business impact of your projects—add the 'why' behind them",
        "In some bullets, list what problems you solved or what goals were achieved (e.g., how did your pipeline improve decision-making?)",
        "Some achievements could stand out more with quantified results—try to use numbers where possible"
      ]
    } """)

        userPrompt = (f"Resume:\n{resume}\n")
        #f"Job Description:\n{jobdesc}\n\n"
        #f"Technical Analysis:\n{analysis}\n")

        messages = [SystemMessage(content=prompt), HumanMessage(content=userPrompt)]

        try:
            response = self.llm.invoke(messages)
            return json.loads(response.content)
        except Exception as e:
            return f"{e}"

pdf = PDFProcessor.PdfProcessor('kataoka.pdf')


f = FeedBack()
temp = f.generateFeedback(f, pdf.resumeOutput)

print(temp)

print(temp['score'])
print(temp['strengths'])
print(temp['suggestions'])
print(temp['constructive_criticism'])

