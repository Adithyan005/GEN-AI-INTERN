import React, { useState } from 'react';
import './App.css'; // Import CSS from a separate file for better organization
import { useNavigate } from 'react-router-dom'; // Import useNavigate for routing

const AdminLogin = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const correctUsername = "admin";
    const correctPassword = "password123"; // Replace with your actual password

    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();
        if (username === correctUsername && password === correctPassword) {
            navigate('/Stock'); // Ensure this path matches your Routes
        } else {
            alert("Invalid credentials. Please try again.");
        }
    };

    return (
        <div className="container">
            <div className="title">
                <h1>Stock Market Prediction</h1>
                <p>Welcome to our stock market prediction platform. Please log in as admin to access your dashboard.</p>
            </div>

            <div className="login-box">
                <h2>Admin Login</h2>
                <form id="loginForm" onSubmit={handleSubmit}>
                    <div className="textbox">
                        <label htmlFor="username">Username</label>
                        <input 
                            type="text" 
                            id="username" 
                            name="username" 
                            placeholder="Enter Username" 
                            required 
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </div>
                    <div className="textbox">
                        <label htmlFor="password">Password</label>
                        <input 
                            type="password" 
                            id="password" 
                            name="password" 
                            placeholder="Enter Password" 
                            required 
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <button type="submit" className="btn">Login</button>
                </form>
            </div>
        </div>
    );
};

export default AdminLogin;
