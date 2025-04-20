from models import PDFProcessor
from models import ResumeAnalyzer
from models import FeedbackEngine
from services import resume_parser
from services.ai_reviewer import ai_reviewer

class Resume_Controller:
    def __init__(self):
        #self.processor = PDFProcessor()
        #self.analyzer = ResumeAnalyzer()
        #self.feedbacker = FeedbackEngine()
        self.airev = ai_reviewer()

    def run(self):
        resume = resume_parser.parser("kataoka.pdf")
        feedback = self.airev.generateFeedback(self.airev, resume)
        print(feedback)

