import { useAuth0 } from '@auth0/auth0-react';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

interface ICoinContext {
  children: any;
  authToken: string;
  getHeaders: () => any;
}

const API_URL = process.env['REACT_APP_API_URL'] || 'localhost:8000';
const CoinContext = React.createContext<ICoinContext>(null as any);

export const CoinProvider = ({ children }: { children: any }) => {
  const { user, isAuthenticated, getAccessTokenSilently } = useAuth0();
  const [authToken, setAuthToken] = useState<string>('invalid token');

  const getHeaders = () => {
    return { headers: { Authorization: `Bearer ${authToken}` } };
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
      }}
    >
      {children}
    </CoinContext.Provider>
  );
};

export default CoinContext;
