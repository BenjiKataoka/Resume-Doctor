import React, { useState, useCallback, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import Typewriter from './Typewriter';
import './App.css';

function AnimatedTitle() {
  return (
    <h1 className="animated-title">
      <Typewriter text="Resume Doctor" speed={70} as="span" />
    </h1>
  );
}

function SequentialFeedback({ feedback }) {
  const [show, setShow] = useState([false, false, false, false]);

  useEffect(() => {
    if (!feedback || feedback.error) return;
    setShow([false, false, false, false]);
    let timers = [];
    timers.push(setTimeout(() => setShow([true, false, false, false]), 400));
    timers.push(setTimeout(() => setShow([true, true, false, false]), 1200));
    timers.push(setTimeout(() => setShow([true, true, true, false]), 2000));
    timers.push(setTimeout(() => setShow([true, true, true, true]), 2800));
    return () => timers.forEach(clearTimeout);
  }, [feedback]);

  if (!feedback || feedback.error) return null;

  return (
    <div className="feedback-container">
      {show[0] && (
        <div className="feedback-section score fade-in">
          <h3>Score</h3>
          <Typewriter
            text={`${feedback.score} / 10`}
            speed={40}
            className="score-type"
          />
        </div>
      )}
      {show[1] && (
        <div className="feedback-section fade-in">
          <h3>Strengths</h3>
          <ul>
            {feedback.strengths && feedback.strengths.map((s, i) =>
              <li key={i}>
                <Typewriter
                  text={s}
                  speed={18}
                />
              </li>
            )}
          </ul>
        </div>
      )}
      {show[2] && (
        <div className="feedback-section fade-in">
          <h3>Suggestions</h3>
          <ul>
            {feedback.suggestions && feedback.suggestions.map((s, i) =>
              <li key={i}>
                <Typewriter
                  text={s}
                  speed={18}
                />
              </li>
            )}
          </ul>
        </div>
      )}
      {show[3] && (
        <div className="feedback-section fade-in">
          <h3>Constructive Criticism</h3>
          <ul>
            {feedback.constructive_criticism && feedback.constructive_criticism.map((c, i) =>
              <li key={i}>
                <Typewriter
                  text={c}
                  speed={18}
                />
              </li>
            )}
          </ul>
        </div>
      )}
    </div>
  );
}

function App() {
  const [feedback, setFeedback] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [fileName, setFileName] = useState('');

  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    if (file) {
      setFileName(file.name);
      setLoading(true);
      setError(null);
      setFeedback(null);

      const formData = new FormData();
      formData.append('resume', file);

      axios.post('http://localhost:5001/api/feedback', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(response => {
        setFeedback(response.data);
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to get feedback. Please try again.');
        setLoading(false);
      });
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'application/pdf': ['.pdf'] }
  });

  return (
    <div className="App dark-theme">
      <header className="App-header">
        <AnimatedTitle />
        <p className="subtitle">Upload your resume to get AI-powered feedback!</p>
      </header>
      <main role="main">
        <div
          {...getRootProps({ className: `dropzone ${isDragActive ? 'active' : ''}` })}
          tabIndex={0}
          aria-label="Resume upload area"
        >
          <input {...getInputProps()} />
          {
            fileName ? <p>{fileName}</p> :
            isDragActive ?
              <p>Drop the file here ...</p> :
              <p>Drag & drop your resume here, or click to select a file</p>
          }
        </div>
        {loading && <div className="loader" aria-live="polite"></div>}
        {error && <div className="error-message" role="alert">{error}</div>}
        {feedback && feedback.error && (
          <div className="error-message" role="alert">
            <h2>Error</h2>
            <p>{feedback.error}</p>
          </div>
        )}
        <SequentialFeedback feedback={feedback} />
      </main>
      <footer>
        <p>Made with ❤️ by Resume Doctor</p>
      </footer>
    </div>
  );
}

export default App; 