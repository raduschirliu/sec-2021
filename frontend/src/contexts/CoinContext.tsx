import { useAuth0 } from '@auth0/auth0-react';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import ICoin from '../models/Coin';
import IPortfolio from '../models/Portfolio';

interface ICoinContext {
  children: any;
  authToken: string;
  getHeaders: () => any;
  getCoinList: () => Promise<ICoin[]>;
  getPortfolios: () => Promise<IPortfolio[]>;
  addPortfolio: (name: string) => Promise<any>;
  activePortfolio: string;
  setActivePortfolio: (portfolio: string) => void;
  getWatchList: () => Promise<ICoin[]>;
  addWatch: (coinId: string) => Promise<any>;
}

const API_URL = process.env['REACT_APP_API_URL'] || 'localhost:8000';
const CoinContext = React.createContext<ICoinContext>(null as any);

export const CoinProvider = ({ children }: { children: any }) => {
  const { user, isAuthenticated, getAccessTokenSilently } = useAuth0();
  const [authToken, setAuthToken] = useState<string>('invalid token');
  const [activePortfolio, setActivePortfolio] = useState<string>('');

  const getHeaders = () => {
    return { headers: { Authorization: `Bearer ${authToken}` } };
  };

  const getCoinList = () => {
    return axios
      .get(`${API_URL}/coinlist`)
      .then((res: any) => res.data as ICoin[]);
  };

  const getPortfolios = () => {
    return axios
      .get(`${API_URL}/portfolios/${user?.sub}`, getHeaders())
      .then((res: any) =>
        res.data?.map(
          (p: any) => ({ id: p[0], user_id: p[1], name: p[2] } as IPortfolio)
        )
      );
  };

  const addPortfolio = (name: string) => {
    return axios.post(
      `${API_URL}/portfolios/${user?.sub}/${name}`,
      {},
      getHeaders()
    );
  };

  const getWatchList = () => {
    return axios
      .get(`${API_URL}/watchlist/${activePortfolio}`, getHeaders())
      .then((res: any) => res.data as ICoin[]);
  };

  const addWatch = (coinId: string) => {
    return axios.post(
      `${API_URL}/watchlist/${activePortfolio}/${coinId}`,
      {},
      getHeaders()
    );
  };

  useEffect(() => {
    if (!isAuthenticated) return;
    getAccessTokenSilently().then(setAuthToken).catch(alert);
  }, [isAuthenticated, getAccessTokenSilently]);

  return (
    <CoinContext.Provider
      value={{
        children,
        authToken,
        getHeaders,
        activePortfolio,
        setActivePortfolio,
        getCoinList,
        getPortfolios,
        addPortfolio,
        getWatchList,
        addWatch,
      }}
    >
      {children}
    </CoinContext.Provider>
  );
};

export default CoinContext;
