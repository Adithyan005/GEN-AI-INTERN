import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [formData, setFormData] = useState({
        OpenPrice: '',
        HighPrice: '',
        LowPrice: '',
        Volume: '',
        MovingAverage10: '',
        MovingAverage50: '',
        RSI: '',
        MACD: '',
        Volatility: ''
    });
    const [prediction, setPrediction] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', formData);
            setPrediction(response.data);
        } catch (error) {
            console.error("Error making prediction", error);
        }
    };

    return (
        <div className="App">
            <h1>Stock Price Prediction</h1>
            <form onSubmit={handleSubmit}>
                {Object.keys(formData).map((key) => (
                    <div key={key}>
                        <label>{key}</label>
                        <input
                            type="number"
                            name={key}
                            value={formData[key]}
                            onChange={handleChange}
                            required
                        />
                    </div>
                ))}
                <button type="submit">Predict</button>
            </form>
            {prediction && (
                <div>
                    <h2>Prediction Results</h2>
                    <p>Predicted Close Price: {prediction.predicted_close_price}</p>
                    <p>Price Movement: {prediction.price_movement === 1 ? 'Increase' : 'Decrease'}</p>
                </div>
            )}
        </div>
    );
}

export default App;
