
import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';

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
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/')
            .then(response => response.json())
            .then(data => setData(data.message));
    }, []);

    return (
        <div>
            <h1>{data}</h1>
        </div>
    );
}

export default App;
