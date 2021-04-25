import logo from './logo.svg';
import './App.css';
import Form from './Form.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Serve Superset Dashboards with ease!
        </p>
        <Form />      
      </header>
    </div>
  );
}

export default App;
