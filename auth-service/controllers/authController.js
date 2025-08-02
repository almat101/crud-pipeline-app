export const login = async (req, res) => {
    //testing route
    try {
        console.log("test login")
        console.log(req.body);
        res.status(200).json({message: "body received" , body_richiesta: req.body})
    } catch (error) {
        res.status(500).json({message: "Internal server error"})
    }
}