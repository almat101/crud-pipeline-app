

const Logout = () => {
    const handleClick = () => {
        console.log("logout logic");
        localStorage.clear();
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