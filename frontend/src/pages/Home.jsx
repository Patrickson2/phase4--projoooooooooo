import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container">
      <div className="hero">
        <h1>Welcome to EventMate</h1>
        <p>Discover, create, and manage amazing events</p>
        <div className="hero-buttons">
          <Link to="/events" className="btn btn-primary">Browse Events</Link>
          <Link to="/register" className="btn btn-secondary">Get Started</Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
