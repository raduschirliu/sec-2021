import { Link } from 'react-router-dom';
import './HomePage.css';

const Home = () => {
  return (
    <div className="home-page">
      <Link to="/portfolio" className="home-account">
        Sign Up or Login
      </Link>
    </div>
  );
};

export default Home;
