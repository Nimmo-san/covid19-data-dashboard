
import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import {Bar} from 'react-chartjs-2'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}


function App() {
    const [chartData, setChartData] = useState({});

    useEffect(() => {
        fetch('http://127.0.0.1:5000/covid-data')
            .then(response => response.json())
            .then(data => {
                setChartData({
                    labels: data.countries,
                    datasets: [
                        {
                            label: 'Total Cases',
                            data: data.total_cases,
                            backgroundColor: 'rgba(75,192,192,0.6)'
                        }
                    ]
                });
            });
    }, []);

    return (
        <div>
            <Bar data={chartData} />
        </div>
    );
}
export default App;
