# Resume Doctor

Resume Doctor is an AI-powered resume review web application. Upload your resume as a PDF and receive actionable, detailed feedback instantly.

## Features
- Drag-and-drop PDF upload
- AI-generated feedback (score, strengths, suggestions, constructive criticism)
- Modern, dark-themed, responsive UI
- Seamless transitions and typewriter effect for feedback

## Tech Stack
- **Frontend:** React.js
- **Backend:** Python (Flask, LangChain, OpenAI)

## Getting Started

### Backend
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=your-key-here
   ```
3. Start the backend:
   ```bash
   python app.py
   ```
   The backend will run on `http://localhost:5001`.

### Frontend
1. Go to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend:
   ```bash
   npm start
   ```
   The frontend will run on `http://localhost:3000`.

## Project Structure
- `app.py` — Flask backend
- `models/` — PDF processing and feedback engine
- `frontend/` — React app (see `src/` for main code)

## Notes
- Do not commit `.venv/`, `node_modules/`, or `kataoka.pdf` (see `.gitignore`).
- For development, use your own OpenAI API key.

---

Made with ❤️ by Resume Doctor
