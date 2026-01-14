import { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { eventsAPI, participationAPI, reviewsAPI } from '../services/api';
import { AuthContext } from '../context/AuthContext';

const EventDetail = () => {
  const { id } = useParams();
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();
  const [event, setEvent] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [rating, setRating] = useState(5);
  const [comment, setComment] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    eventsAPI.getOne(id).then(res => setEvent(res.data));
    reviewsAPI.getByEvent(id).then(res => setReviews(res.data));
  }, [id]);

  const handleJoin = async () => {
    try {
      await participationAPI.join(id);
      setMessage('Successfully joined event!');
    } catch (err) {
      setMessage(err.response?.data?.detail || 'Failed to join');
    }
  };

  const handleReview = async (e) => {
    e.preventDefault();
    try {
      await reviewsAPI.create({ event_id: parseInt(id), rating, comment });
      setMessage('Review submitted!');
      setComment('');
      reviewsAPI.getByEvent(id).then(res => setReviews(res.data));
    } catch (err) {
      setMessage('Failed to submit review');
    }
  };

  const handleDelete = async () => {
    if (window.confirm('Delete this event?')) {
      try {
        await eventsAPI.delete(id);
        navigate('/my-events');
      } catch (err) {
        setMessage('Failed to delete event');
      }
    }
  };

  if (!event) return <div className="loading">Loading...</div>;

  return (
    <div className="container">
      <div className="event-detail">
        <h1>{event.title}</h1>
        <p>{event.description}</p>
        <div className="event-info">
          <div className="event-info-item">
            <strong>Location</strong>
            <span>{event.location}</span>
          </div>
          <div className="event-info-item">
            <strong>Date & Time</strong>
            <span>{new Date(event.datetime).toLocaleString()}</span>
          </div>
        </div>
        {message && <div className="success-message">{message}</div>}
        <div className="card-actions">
          {user && user.id !== event.organizer_id && (
            <button onClick={handleJoin} className="btn btn-primary">Join Event</button>
          )}
          {user && user.id === event.organizer_id && (
            <button onClick={handleDelete} className="btn btn-danger">Delete Event</button>
          )}
        </div>
      </div>

      <div className="reviews-section">
        <h2>Reviews</h2>
        {reviews.map(review => (
          <div key={review.id} className="review-card">
            <div className="review-rating">⭐ {review.rating}/5</div>
            <p className="review-comment">{review.comment}</p>
          </div>
        ))}

        {user && (
          <div className="form-container">
            <h3>Leave a Review</h3>
            <form onSubmit={handleReview}>
              <div className="form-group">
                <label>Rating</label>
                <select value={rating} onChange={(e) => setRating(e.target.value)}>
                  <option value="5">5 - Excellent</option>
                  <option value="4">4 - Good</option>
                  <option value="3">3 - Average</option>
                  <option value="2">2 - Poor</option>
                  <option value="1">1 - Terrible</option>
                </select>
              </div>
              <div className="form-group">
                <label>Comment</label>
                <textarea
                  value={comment}
                  onChange={(e) => setComment(e.target.value)}
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary">Submit Review</button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
};

export default EventDetail;
