import { useAuth0 } from '@auth0/auth0-react';
import axios from 'axios';
import { useContext, useEffect, useState } from 'react';
import Nav from '../../components/Nav/Nav';
import CoinContext from '../../contexts/CoinContext';
import './PortfolioPage.css';

const API_URL = process.env.REACT_APP_API_URL;

const PortfolioPage = () => {
  const { user, isAuthenticated } = useAuth0();
  const { getHeaders } = useContext(CoinContext);

  useEffect(() => {
    // Test logins
    axios
      .post(`${API_URL}/account`, {}, getHeaders())
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [getHeaders]);

  return (
    <div className="account-page">
      <Nav />
    </div>
  );
};

export default PortfolioPage;
