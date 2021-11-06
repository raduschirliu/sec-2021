import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from '../../pages/Home/Home';
import './App.css';

const App = () => {
  return (
    <div className="app-container">
      <Router>
        <Switch>
          <Route path="/" component={Home} exact />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
