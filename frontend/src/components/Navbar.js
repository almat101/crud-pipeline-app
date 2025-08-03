import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav style={{ padding: '10px', backgroundColor: '#ddd', display: 'flex', justifyContent: 'space-around' }}>
      <Link to="/signup">Signup</Link>
      <Link to="/login">Login</Link>
      <Link to="/products">Products</Link>
    </nav>
  );
};

export default Navbar;