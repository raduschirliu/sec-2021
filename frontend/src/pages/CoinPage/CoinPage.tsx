import { useAuth0 } from '@auth0/auth0-react';
import axios from 'axios';
import { DataGrid, GridRowParams, MuiEvent } from '@mui/x-data-grid';
import { useContext, useEffect, useState } from 'react';
import CoinContext from '../../contexts/CoinContext';
import ICoin from '../../models/Coin';
import './CoinPage.css';
import { Box } from '@mui/system';
import { Button, CircularProgress } from '@mui/material';

const CoinPage = () => {
  const { getCoinList, addWatch } = useContext(CoinContext);
  const [coins, setCoins] = useState<ICoin[]>([]);
  const [loading, setLoading] = useState(true);

  console.log(coins);

  const renderWatchCell = (params: any) => {
    console.log(params);
    return (
      <Button onClick={() => {}} variant="outlined">
        Watch
      </Button>
    );
  };

  useEffect(() => {
    getCoinList()
      .then(setCoins)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [getCoinList, setCoins]);

  return (
    <div className="coin-page">
      {loading ? (
        <Box sx={{ display: 'flex' }}>
          <CircularProgress />
        </Box>
      ) : (
        <DataGrid
          onRowClick={(params: GridRowParams, event: any) => {
            addWatch(params.row['id'])
              .then(() => alert('added to watch list'))
              .catch(console.error);
          }}
          rows={coins}
          columns={[
            {
              field: 'symbol',
              flex: 1,
              headerName: 'Symbol',
            },
            {
              field: 'name',
              flex: 1,
              headerName: 'Name',
            },
            // {
            //   field: 'Watch',
            //   width: 150,
            //   renderCell: renderWatchCell,
            // },
          ]}
          pageSize={100}
        />
      )}
    </div>
  );
};

export default CoinPage;
