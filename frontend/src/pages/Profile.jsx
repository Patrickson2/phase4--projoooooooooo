import { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

const Profile = () => {
  const { user } = useContext(AuthContext);

  return (
    <div className="container">
      <div className="form-container">
        <h2 className="form-title">My Profile</h2>
        <div className="form-group">
          <label>Name</label>
          <input type="text" value={user?.name || ''} disabled />
        </div>
        <div className="form-group">
          <label>Email</label>
          <input type="email" value={user?.email || ''} disabled />
        </div>
        <div className="form-group">
          <label>Role</label>
          <input type="text" value={user?.role || ''} disabled />
        </div>
        <div className="form-group">
          <label>Member Since</label>
          <input
            type="text"
            value={user?.created_at ? new Date(user.created_at).toLocaleDateString() : ''}
            disabled
          />
        </div>
      </div>
    </div>
  );
};

export default Profile;
