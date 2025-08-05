import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';


const Navbar = () => {
  const { isAuth } = useContext(AuthContext);
  return (
    <nav style={{ padding: '10px', backgroundColor: '#ddd', display: 'flex', justifyContent: 'space-around' }}>
      { !isAuth && <Link to="/signup">Signup</Link> }
      { !isAuth &&<Link to="/login">Login</Link> }
      { isAuth &&<Link to="/products">Products</Link> }
      { isAuth &&<Link to="/logout">Logout</Link> }
    </nav>
  );
};

export default Navbar;