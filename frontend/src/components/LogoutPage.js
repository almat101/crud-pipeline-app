import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from 'react-router-dom'

const Logout = () => {

    const { logout, deleteId } = useContext(AuthContext);

    const navigate = useNavigate();

    const handleClick = () => {

        console.log("logout logic");
        // remove token from local storage
        logout();
        // delete id from local storage
        deleteId();
        
        navigate('/login');
    }

    return (
        <div style={{ display: "flex", justifyContent: "center", alignItems: "center", height: "10vh" }}>
            <button
                style={{
                    padding: "8px 16px",
                    background: "#d21919ff",
                    color: "#fff",
                    border: "none",
                    borderRadius: "4px",
                    cursor: "pointer",
                    fontSize: "16px"
                }}
                onClick={handleClick}
            >
                Logout
            </button>
        </div>
    );
};

export default Logout;