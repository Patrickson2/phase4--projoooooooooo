import { useState, useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';
import { eventsAPI } from '../services/api';
import { AuthContext } from '../context/AuthContext';

const MyEvents = () => {
  const { user } = useContext(AuthContext);
  const [events, setEvents] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [location, setLocation] = useState('');
  const [datetime, setDatetime] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    loadEvents();
  }, []);

  const loadEvents = () => {
    eventsAPI.getAll().then(res => {
      const myEvents = res.data.filter(e => e.organizer_id === user.id);
      setEvents(myEvents);
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await eventsAPI.create({ title, description, location, datetime });
      setMessage('Event created successfully!');
      setShowForm(false);
      setTitle('');
      setDescription('');
      setLocation('');
      setDatetime('');
      loadEvents();
    } catch (err) {
      setMessage('Failed to create event');
    }
  };

  return (
    <div className="container">
      <h1>My Events</h1>
      <button onClick={() => setShowForm(!showForm)} className="btn btn-primary">
        {showForm ? 'Cancel' : 'Create New Event'}
      </button>

      {showForm && (
        <div className="form-container">
          <h2 className="form-title">Create Event</h2>
          {message && <div className="success-message">{message}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Title</label>
              <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label>Description</label>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label>Location</label>
              <input
                type="text"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label>Date & Time</label>
              <input
                type="datetime-local"
                value={datetime}
                onChange={(e) => setDatetime(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="btn btn-primary" style={{width: '100%'}}>
              Create Event
            </button>
          </form>
        </div>
      )}

      <div className="events-grid">
        {events.length === 0 ? (
          <div className="empty-state">
            <h3>No events created yet</h3>
            <p>Create your first event to get started</p>
          </div>
        ) : (
          events.map(event => (
            <div key={event.id} className="card">
              <h3 className="card-title">{event.title}</h3>
              <p className="card-text">{event.description}</p>
              <p className="card-text">📍 {event.location}</p>
              <p className="card-text">📅 {new Date(event.datetime).toLocaleString()}</p>
              <Link to={`/events/${event.id}`} className="btn btn-primary">
                View Details
              </Link>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default MyEvents;
