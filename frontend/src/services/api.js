import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authAPI = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
  getMe: () => api.get('/auth/me'),
};

export const eventsAPI = {
  getAll: () => api.get('/events'),
  getOne: (id) => api.get(`/events/${id}`),
  create: (data) => api.post('/events', data),
  update: (id, data) => api.patch(`/events/${id}`, data),
  delete: (id) => api.delete(`/events/${id}`),
};

export const participationAPI = {
  join: (eventId) => api.post('/participation', { event_id: eventId }),
  update: (id, status) => api.patch(`/participation/${id}`, { status }),
};

export const reviewsAPI = {
  create: (data) => api.post('/reviews', data),
  getByEvent: (eventId) => api.get(`/reviews/${eventId}`),
  delete: (id) => api.delete(`/reviews/${id}`),
};

export default api;
