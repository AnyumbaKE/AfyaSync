// src/Slider.js

import React, { useState, useEffect } from 'react';
import './Slider.css';

const images = [
  './assets/image1.jpg',
  './assets/image2.jpg',
  './assets/image3.jpg',
  './assets/image4.jpg'
];

const Slider = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prevSlide) => (prevSlide + 1) % images.length);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="slider-container">
      <div
        className="slide-wrapper"
        style={{ transform: `translateX(-${currentSlide * 100}%)` }}
      >
        {images.map((src, index) => (
          <div key={index} className="slide">
            <img src={src} alt={`Slide ${index + 1}`} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Slider;
