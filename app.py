import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile

from models.PDFProcessor import PdfProcessor
from models.FeedbackEngine import FeedBack

app = Flask(__name__)
CORS(app)  # This will allow the frontend to make requests to the backend

feedback_engine = FeedBack()

@app.route('/api/feedback', methods=['POST'])
def get_feedback():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400

    resume_file = request.files['resume']

    if resume_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if resume_file and resume_file.filename.endswith('.pdf'):
        try:
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
                resume_file.save(temp_pdf.name)
                temp_pdf_path = temp_pdf.name

            # Process the PDF to extract text
            pdf_processor = PdfProcessor(temp_pdf_path)
            resume_text = pdf_processor.resumeOutput

            # Generate feedback using the feedback engine
            feedback = feedback_engine.generateFeedback(resume_text)

            # Clean up the temporary file
            os.remove(temp_pdf_path)

            return jsonify(feedback)

        except Exception as e:
            # Clean up the temp file in case of an error
            if 'temp_pdf_path' in locals() and os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type, please upload a PDF'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001) 