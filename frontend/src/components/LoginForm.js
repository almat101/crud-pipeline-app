import { useState, useContext } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'
import { AuthContext }  from '../context/AuthContext'

const isDev = process.env.REACT_APP_IS_DEV === 'true';
 
const URL = isDev ? 'http://localhost:3030/auth/login' : '/auth/login';


console.log(URL)

// const URL_DEV = 'http://localhost:3030/auth/login';
//const URL_PROD = '/auth/login';


const LoginForm = () => {

const { login, saveId } = useContext(AuthContext);
  
  const navigate = useNavigate();
  const [FormData, setFormData] = useState({
    email: '',
    password: ''
  });

  const [message, setMessage] = useState(''); // Stato per messaggi di successo o errore

  const handleChange = (e) => {
    const {name, value} = e.target;
      setFormData({
        ...FormData,
        [name]: value,
      });
  };


   // Gestione del submit del form
    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('Form data:', FormData);
        try {
            const response = await axios.post(`${URL}`, FormData, {
              headers : { 'Content-Type' : 'application/json' },
            });
            setMessage('Signup successful!');
            //destrucuring da un oggetto
            const { token, id } = response.data;
            //salvo id tramite context
            saveId(id);
            //salvo il token tramite context
            login(token);

            navigate('/products');
        } catch (error) {
            setMessage(error.response?.data?.message || 'Signup failed!'); // Mostra un messaggio di errore
            console.error(error.response?.data);
    }
    
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      {message && <p>{message}</p>} {}
      <label>
        Email:
        <input 
          type="email"
          name="email"
          value={FormData.email}
          onChange={handleChange}
        />
      </label>
      <label>
        Password:
        <input
          type="password"
          name="password"
          value={FormData.password}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;