import { useAuth0 } from '@auth0/auth0-react';
import {
  Button,
  CircularProgress,
  TextField,
  Typography,
} from '@material-ui/core';
import { Label } from '@mui/icons-material';
import { Box } from '@mui/system';
import { useContext, useEffect, useState } from 'react';
import CoinContext from '../../contexts/CoinContext';
import ICoin from '../../models/Coin';
import IPortfolio from '../../models/Portfolio';
import './WatchPage.css';

const WatchPage = () => {
  const { user } = useAuth0();
  const { getWatchList, activePortfolio } = useContext(CoinContext);
  const [watchList, setWatchList] = useState<ICoin[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    getWatchList()
      .then(setWatchList)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [getWatchList, setWatchList]);

  return (
    <div className="watch-page">
      <div className="watch-page-list">
        {activePortfolio?.length > 1 ? (
          <>
            <Typography variant="h4">Your watched coins</Typography>
            {loading ? (
              <CircularProgress />
            ) : watchList.length > 0 ? (
              watchList.map((p) => <p className="watch-page-item" key={p.id}>{p.name}</p>)
            ) : (
              <p>
                No watched coins, please go to the coin list to add a watched
                coin
              </p>
            )}
          </>
        ) : (
          <p>No portfolio selected, please create one in the portfolio tab</p>
        )}
      </div>
    </div>
  );
};

export default WatchPage;
