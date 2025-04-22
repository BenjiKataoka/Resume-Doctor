from models import PDFProcessor
from models import ResumeAnalyzer
from models import FeedbackEngine

class Resume_Controller:
    def __init__(self, path: str):
        self.processor = PDFProcessor.PdfProcessor(path)
        self.feedbackEngine = FeedbackEngine.FeedBack()
        self.resume = ResumeAnalyzer.Resume

    def run(self):
        parsedResume = self.processor.resumeOutput
        feedback =  self.feedbackEngine.generateFeedback(self.feedbackEngine, parsedResume)
        resume = self.resume.setter(feedback)

