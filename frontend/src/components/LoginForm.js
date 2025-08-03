import { useState } from 'react';
import axios from 'axios';
import {useNavigate} from 'react-router-dom'

const LoginForm = () => {
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
            const response = await axios.post('/auth/login', FormData, {
              headers : { 'Content-Type' : 'application/json' },
            });
            setMessage('Signup successful!');
            console.log(response.data); // Per debug
            navigate('/products');
        } catch (error) {
            setMessage(error.response?.data?.message || 'Signup failed!'); // Mostra un messaggio di errore
            console.error(error.response?.data); // Per debug
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