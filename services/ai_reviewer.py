#temporpdsajkjsoldfasf
from dotenv import load_dotenv

load_dotenv()

import os

from langchain_core.messages import SystemMessage, HumanMessage

from services import resume_parser
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


class ai_reviewer:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.7,
            model="gpt-3.5-turbo",
            openai_api_key = os.getenv("OPENAI_API_KEY")
        )

    @staticmethod
    def generateFeedback(self, resume: str) -> str:
        #    def generateFeedback(self, analysis: dict, resume: str, jobdesc: str) -> str:
        prompt = ("""
        You are an expert tech recruiter reviewing resumes for a software engineer role and your client is in dire need of your help!"
                      "Given this resume: { resume },":

        - A "score" out of 10 indicating the resume's strength.
        - A list of specific "strengths".
        - A list of actionable "suggestions" for improvement as well as constructive criticism.

        Example:
        {
            "score": 8.5,
            "strengths": ["Relevant work experience", "Strong educational background"],
            "suggestions": ["Add measurable results to experience bullet points", "Include a summary section"
            "Constructive Criticism": ["Give me the why of these projects and your impact"]]
        } """)

        resume_parser.parser("kataoka.pdf")
        userPrompt = (f"Resume:\n{resume}\n")
        #f"Job Description:\n{jobdesc}\n\n"
         #f"Technical Analysis:\n{analysis}\n")

        messages = [SystemMessage(content=prompt), HumanMessage(content=userPrompt)]

        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            return f"{e}"


