import { useState} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const URL_DEV = 'http://localhost:3030/auth/signup';
//const URL_PROD = '/auth/signup';

const SignupForm = () => {
    const navigate = useNavigate();
    //stato iniziale del form
    const [ FormData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        repeat_password: '',
    });

    const [message, setMessage] = useState(''); // Stato per messaggi di successo o errore
    
    //gestione dei cambiamenti nei campi
    const handleChange = (e) => {
    const { name, value} = e.target;
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
            const response = await axios.post(`${URL_DEV}`, FormData, {
              headers : { 'Content-Type' : 'application/json' },
            });
            setMessage('Signup successful!');
            console.log(response.data); // Per debug
            navigate('/login');
        } catch (error) {
            setMessage(error.response?.data?.message || 'Signup failed!'); // Mostra un messaggio di errore
            console.error(error.response?.data); // Per debug
    }
    
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Signup</h2>
        {message && <p>{message}</p>} {}
      <label>
        Username:
        <input
            type="text"
            name="username"
            value={FormData.username} 
            onChange={handleChange}
        />
      </label>
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
      <label>
        Repeat Password:
        <input
          type="password"
          name="repeat_password"
          value={FormData.repeat_password}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Signup</button>
    </form>
  );
};

export default SignupForm;