import { withAuthenticationRequired } from '@auth0/auth0-react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { CoinProvider } from '../../contexts/CoinContext';
import CoinPage from '../../pages/CoinPage/CoinPage';
import HomePage from '../../pages/HomePage/HomePage';
import PortfolioPage from '../../pages/PortfolioPage/PortfolioPage';
import WatchPage from '../../pages/WatchPage/WatchPage';
import Nav from '../Nav/Nav';
import './App.css';

const GuardedRoute = ({ component, ...rest }: any) => {
  return <Route component={withAuthenticationRequired(component)} {...rest} />;
};

const App = () => {
  return (
    <div className="app-container">
      <CoinProvider>
        <Router>
          <Nav />
          <Switch>
            {/* Logged in routes */}
            <GuardedRoute path="/portfolio" component={PortfolioPage} />
            <GuardedRoute path="/coinlist" component={CoinPage} />
            <GuardedRoute path="/watch" component={WatchPage} />

            {/* Home route, no login */}
            <Route path="/" component={HomePage} exact />
          </Switch>
        </Router>
      </CoinProvider>
    </div>
  );
};

export default App;
