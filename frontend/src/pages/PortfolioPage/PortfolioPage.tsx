import { useAuth0 } from '@auth0/auth0-react';
import {
  Button,
  CircularProgress,
  TextField,
  Typography,
} from '@material-ui/core';
import { useContext, useEffect, useState } from 'react';
import CoinContext from '../../contexts/CoinContext';
import IPortfolio from '../../models/Portfolio';
import './PortfolioPage.css';

const PortfolioPage = () => {
  const { user } = useAuth0();
  const { getPortfolios, addPortfolio, activePortfolio, setActivePortfolio } =
    useContext(CoinContext);
  const [portfolios, setPortfolios] = useState<IPortfolio[]>([]);
  const [portfolioName, setPortfolioName] = useState('');
  const [loading, setLoading] = useState(false);

  const createPortfolio = () => {
    addPortfolio(portfolioName)
      .then(() => {
        setPortfolioName('');
        alert('added portfolio');
      })
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    setLoading(true);
    getPortfolios()
      .then(setPortfolios)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [getPortfolios, setPortfolios]);

  return (
    <div className="portfolio-page">
      <div className="portfolio-page-new">
        <Typography variant="h4">Create a new portfolio</Typography>
        <TextField
          label="Name"
          variant="outlined"
          onChange={(e) => setPortfolioName(e.target.value)}
          value={portfolioName}
        ></TextField>
        <Button variant="outlined" onClick={createPortfolio}>Create</Button>
      </div>
      <div className="portfolio-page-list">
        <Typography variant="h4">Your portfolios</Typography>
        {loading ? (
          <CircularProgress />
        ) : portfolios.length > 0 ? (
          portfolios.map((p) => (
            <div key={p.id} className="portfolio-page-portfolio">
              <p>{p.name}</p>
              {activePortfolio === p.id ? (
                <Button variant="outlined" disabled={true}>
                  Selected
                </Button>
              ) : (
                <Button
                  variant="outlined"
                  onClick={() => setActivePortfolio(p.id)}
                >
                  Select
                </Button>
              )}
            </div>
          ))
        ) : (
          <p>No portfolios, please create one above</p>
        )}
      </div>
    </div>
  );
};

export default PortfolioPage;
