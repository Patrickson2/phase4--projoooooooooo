import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Dashboard = () => {
  const { user } = useContext(AuthContext);

  return (
    <div className="container">
      <h1>Welcome, {user?.name}!</h1>
      
      <div className="dashboard-section">
        <h2>Quick Actions</h2>
        <div className="events-grid">
          <div className="card">
            <h3 className="card-title">Browse Events</h3>
            <p className="card-text">Discover upcoming events</p>
            <Link to="/events" className="btn btn-primary">View Events</Link>
          </div>
          <div className="card">
            <h3 className="card-title">My Events</h3>
            <p className="card-text">Manage your created events</p>
            <Link to="/my-events" className="btn btn-primary">View My Events</Link>
          </div>
          <div className="card">
            <h3 className="card-title">Profile</h3>
            <p className="card-text">Update your information</p>
            <Link to="/profile" className="btn btn-primary">View Profile</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
