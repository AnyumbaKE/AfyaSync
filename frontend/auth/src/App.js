import React from 'react';
import { Route, Routes } from 'react-router-dom';
// eslint-disable-next-line
import Public from './components/Public';
import Login from './features/auth/Login';

/**
 * Main application component that sets up routing for the application.
 * This component uses React Router to define public and private routes.
 */
function App() {
  return (
    <Routes>
      <Route path="login" element={<Login />} />
      <Route index element={<Login />} />
        {/* public routes*/}
        
        {/* private routes*/}
    </Routes>
  );
}

export default App;