import controllers.Resume_Controller
from controllers.Resume_Controller import Resume_Controller
from services import resume_parser
from services.ai_reviewer import ai_reviewer
from services import ai_reviewer

#kat = resume_parser.parser("kataoka.pdf")

from dotenv import load_dotenv
import os

load_dotenv()
#
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY)
#print(OPENAI_API_KEY)

x = Resume_Controller()
Resume_Controller.run(x)