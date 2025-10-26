## Project Summary

I started this project to learn Node.js by building a **CRUD** application. The initial version implemented the basic HTTP methods—Create (POST), Read (GET), Update (PATCH/PUT), and Delete (DELETE)—using a **microservices architecture**.

After setting up the basic CRUD microservice, I added an **authentication microservice** in Node.js to handle user login and signup. The /auth/login endpoint generates a `JWT` token upon successful login, which I store in localStorage for simplicity (though cookies would be more secure in production). For signup, I used `Joi` for user validation, and for login, I used `bcrypt` to hash passwords.
I also implemented a `middleware` for the products microservice that checks for a valid `JWT` token. If the token is missing or invalid, the middleware returns a 401 error. This ensures that only authenticated users can access product endpoints.

For the frontend, I created a `React app` (as another microservice) and used `Nginx` to serve the React build and act as a reverse proxy for the backend microservices.

After this CRUD and authentication foundation, I was inspired by an interview with a Milan-based startup working on data scraping and analytics for hotels and B&Bs. I decided to expand my project by introducing a `data pipeline` (ELTL architecture):

- **Scraper microservice**: Uses `Selenium` to scrape product data from an e-commerce site and saves the raw (immutable) data to `MongoDB`, which is well-suited for storing JSON documents.
- **Transformer microservice**: Reads the raw data from MongoDB, cleans and processes it using `Pandas` and `NumPy`, and then saves the cleaned data to `PostgreSQL`.
- **Orchestrator microservice**: Exposes an endpoint that triggers the pipeline, first calling the scraper and then the transformer. The orchestrator accepts both a `path parameter` and a `query string` to mimic the original e-commerce search functionality.
- In the first version, I had another microservice that used a CRON job to automatically trigger the pipeline at startup and every hour. However, in that version, only hardcoded data was scraped.
- In the current version, I added a button to the React frontend that allows users to dynamically search for products by specifying the product name and category. This sends a request to the orchestrator, which coordinates the scraping and transformation steps.


This project demonstrates how a simple CRUD app can evolve into a more complex system combining authentication, frontend integration, and a scalable data pipeline inspired by real-world architectures.