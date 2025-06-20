import React, { useEffect, useState } from 'react';

export default function Typewriter({ text, onDone, speed = 25, as = 'p', className = '' }) {
  const [displayed, setDisplayed] = useState('');
  useEffect(() => {
    setDisplayed('');
    let i = 0;
    if (!text) {
      onDone && onDone();
      return;
    }
    const interval = setInterval(() => {
      setDisplayed(text.slice(0, i + 1));
      i++;
      if (i === text.length) {
        clearInterval(interval);
        onDone && onDone();
      }
    }, speed);
    return () => clearInterval(interval);
    // eslint-disable-next-line
  }, [text]);
  const Tag = as;
  return <Tag className={className}>{displayed}</Tag>;
} 