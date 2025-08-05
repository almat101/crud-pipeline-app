import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import './App.css';
import Header from './components/Header';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import SignupForm from './components/SignupForm';
import LoginForm from './components/LoginForm';
import ProductPage from './components/ProductPage'
import LogoutPage from './components/LogoutPage'
import { AuthProvider } from './context/AuthContext'

function App() {
  return (

    <AuthProvider>

    <Router>
      <div className="App">
        <Header />
        <Navbar />
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/signup" element={<SignupForm />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path='/products' element={<ProductPage />} />
          <Route path='/logout' element={<LogoutPage />} />

        </Routes>
        <Footer />
      </div>
    </Router>

    </AuthProvider>
  );
}

export default App;