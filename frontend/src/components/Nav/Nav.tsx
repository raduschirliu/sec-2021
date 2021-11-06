import { useAuth0 } from '@auth0/auth0-react';
import {
  Box,
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  MenuItem,
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import { Link } from 'react-router-dom';
import './Nav.css';

const Nav = () => {
  const { user, logout } = useAuth0();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          {user ? (
            <>
              <Typography variant="h6" color="inherit" component="div" sx={{ mr: 10 }}>
                CryptoCache     
              </Typography>
              <MenuItem component={Link} to="/portfolio" sx={{ mr: 4 }}>
                Portfolios     
              </MenuItem>
              <MenuItem component={Link} to="/coinlist" sx={{ mr: 4 }}>
                Coins     
              </MenuItem>
              <MenuItem component={Link} to="/watch" sx={{ mr: 4 }}>
                Watchlist     
              </MenuItem>
              <MenuItem onClick={() => logout()}>Logout</MenuItem>
            </>
          ) : (
            <>
              {/* TODO: Make nicer */}
              <MenuItem component={Link} to="/portfolio">
                Login
              </MenuItem>
            </>
          )}
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Nav;
