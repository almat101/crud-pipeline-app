// Importo Router 
import { Router } from "express";
import { login } from "../controllers/authController.js";
// Definisco una costante router
const router =  Router();

//creo la rotta con la chiamata al controller
//endpoint da chiamata localhost:3030/auth/login
router.post('/login', login);

//esporto il router per prenderlo in app.js
export default router;