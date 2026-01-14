import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { eventsAPI } from '../services/api';

const Events = () => {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    eventsAPI.getAll()
      .then(res => setEvents(res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="loading">Loading events...</div>;

  return (
    <div className="container">
      <h1>All Events</h1>
      {events.length === 0 ? (
        <div className="empty-state">
          <h3>No events available</h3>
          <p>Check back later for upcoming events</p>
        </div>
      ) : (
        <div className="events-grid">
          {events.map(event => (
            <div key={event.id} className="card">
              <h3 className="card-title">{event.title}</h3>
              <p className="card-text">{event.description}</p>
              <p className="card-text">📍 {event.location}</p>
              <p className="card-text">📅 {new Date(event.datetime).toLocaleString()}</p>
              <div className="card-actions">
                <Link to={`/events/${event.id}`} className="btn btn-primary">
                  View Details
                </Link>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Events;
