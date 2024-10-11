import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AdminLogin from './AdminLogin'; // Adjust the path as necessary
import  Stock from './Stock'; // Adjust the path as necessary
import './App.css';

const App = () => {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<AdminLogin />} />
                    <Route path="/Stock" element={<Stock />} /> {/* Ensure the path is correct */}
                </Routes>
            </div>
        </Router>
    );
};

export default App;
