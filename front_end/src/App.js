import logo from './logo.svg';
import Dashboard from './components/Dashboard/Dashboard';
import Profile from './components/Profile/Profile';
import Subscription from './components/Subscription/Subscription';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/index" element={<Navigate replace to="/" />} />
          <Route path="/" element={<Dashboard />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/subscription" element={<Subscription />} />
          {/* Fallback for any other URL */}
          <Route path="*" element={<Navigate replace to="/" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
