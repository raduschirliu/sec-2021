import { withAuthenticationRequired } from '@auth0/auth0-react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { CoinProvider } from '../../contexts/CoinContext';
import HomePage from '../../pages/HomePage/HomePage';
import PortfolioPage from '../../pages/PortfolioPage/PortfolioPage';
import './App.css';

const GuardedRoute = ({ component, ...rest }: any) => {
  return <Route component={withAuthenticationRequired(component)} {...rest} />;
};

const App = () => {
  return (
    <div className="app-container">
      <CoinProvider>
        <Router>
          <Switch>
            {/* Logged in routes */}
            <GuardedRoute path="/portfolio" component={PortfolioPage} />

            {/* Home route, no login */}
            <Route path="/" component={HomePage} exact />
          </Switch>
        </Router>
      </CoinProvider>
    </div>
  );
};

export default App;
