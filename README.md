## Full-Stack Data-Driven Pipeline Application

This project started as a simple CRUD application and evolved into a modular system with an integrated data pipeline for scraping, processing, and visualizing e-commerce product data. The system automates data extraction, transformation, and loading (ELTL) processes while maintaining a user-friendly interface for managing and viewing products.

## Project Overview

This project combines a traditional CRUD application with a data-driven pipeline. It scrapes product data from e-commerce sites, processes it, and makes it available for visualization through a React frontend. The architecture is modular, with separate services for scraping, transforming, and orchestrating the pipeline.

## Architecture

The project is built with a modular architecture, with each component serving a specific purpose:


```
├── backend/
│   ├── auth-service/         # Authentication and user management
│   ├── products-service/     # CRUD operations for products
│   ├── scraper-service/      # Extracts raw data from e-commerce sites
│   ├── transformer-service/  # Cleans and transforms raw data
│   └── orchestrator-service/ # Coordinates the data pipeline
├── frontend/                 # React application for user interface
└── cron-service/             # Handles automated pipeline execution
```

## Key Features

### Core CRUD Application

**User Authentication:**
- Secure signup and login functionality with JWT tokens
- Password hashing with bcrypt
- Token-based authentication for protected routes
- User validation with Joi

**Product Management:**
- Create, read, update, and delete product entries
- PostgreSQL database for persistent storage
- Integrated with pg (node-postgres) for seamless database interaction

**RESTful API:**
- Clean API structure following REST principles
- Proper HTTP method usage (GET, POST, PUT, PATCH, DELETE)

### Data Pipeline

**ELTL Architecture:**
- **Extract & Load (1):** A single microservice combines the extraction of product data (using Selenium) and the loading of raw data into MongoDB. This approach simplifies the architecture by reducing the number of microservices while maintaining functionality.
- **Transform & Load (2):** Another microservice handles both the transformation of data (using Pandas for cleaning and standardization) and the loading of processed data into PostgreSQL for application use.

**Automation:**
- Cron job configured to run the pipeline hourly
- Pipeline orchestration through a dedicated microservice

**Data Processing:**
- Price normalization and extraction
- Location data standardization (city, province)
- Text cleaning and filtering based on exact product name

### DevOps Features

**Containerization:**
- Docker containers for each microservice
- Docker Compose for service orchestration
- Environment variable management

**Health Monitoring:**
- Health check endpoints for each service
- Dependency management between services

## Technologies Used

### Backend
- **Node.js & Express:** Core server framework for auth and products services
- **FastAPI (Python):** Powers the data pipeline services
- **PostgreSQL:** Stores processed product data and user information
- **MongoDB:** Stores raw scraped data
- **JWT:** Authentication tokens
- **bcrypt:** Password hashing
- **Joi:** Request validation

### Data Pipeline
- **Selenium:** Web scraping and browser automation
- **Pandas & NumPy:** Data transformation and cleaning
- **SQLAlchemy:** Database ORM for Python services
- **pymongo:** MongoDB interactions from Python

### Frontend
- **React:** UI framework
- **React Bootstrap:** UI components
- **Axios:** HTTP client with interceptors for JWT handling
- **React Router:** Navigation and routing

### DevOps
- **Docker & Docker Compose:** Containerization and orchestration
- **Cron:** Scheduled task execution
- **Nginx:** Reverse proxy (for production)

## Project Evolution

This project evolved over 20 days, with each day focusing on specific enhancements:

- **Days 1-3:** Setting up Node.js, Express, and understanding asynchronous programming
- **Days 4-5:** Implementing CRUD operations with PostgreSQL
- **Days 6-7:** Building the authentication service and frontend setup
- **Days 8-10:** Frontend development, JWT token handling, and UI improvements
- **Days 11-13:** Building the scraper service with Selenium and FastAPI
- **Days 14-15:** MongoDB integration and raw data storage
- **Days 16-17:** Implementing the transformer service with data cleaning
- **Days 18-19:** Containerization and orchestration of the pipeline
- **Day 20:** Automation with cron jobs and final integrations

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for managing virtual environments, if needed in local development)

### Running with Docker Compose

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd express_project_1

# Rename the .env.example file to .env
mv .env.example .env

# Start all services
docker-compose up -d

# For development with hot-reload
docker-compose -f docker-compose.dev.yml up -d
```

### Accessing the Application
- **Frontend:** [http://localhost:80](http://localhost:80)
- **Products API:** [http://localhost:3020/api/products](http://localhost:3020/api/products)
- **Auth API:** [http://localhost:3030/api/auth](http://localhost:3030/api/auth)
- **Scraper API:** [http://localhost:3040/scrape](http://localhost:3040/scrape) (scrape the products and save to mongoDB)
- **Transformer API:** [http://localhost:3050/transform](http://localhost:3050/transform) (clean the products and save to postgreSQL)
- **Orchestrator API:** [http://localhost:3060/orchestrate](http://localhost:3060/orchestrate) (triggers the pipeline)

## Further Documentation

For detailed information about the implementation and evolution of each component, refer to the `docs` directory, which contains day-by-day recaps (`recap_giorno_X.md`) documenting the development process from a simple Express application to a full-featured data pipeline.

## License

This project is licensed under the terms of the license included in the repository.