import Login from './features/auth/Login';
import Public from './components/Public';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route index element={<Login />} />
      
    </Routes>
  );
}

export default App;
