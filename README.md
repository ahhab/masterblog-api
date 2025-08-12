# Masterblog API

This project is a simple blog post API created as an exercise for the Masterschool program. Thank you to Masterschool for providing this excellent learning opportunity and for the well-designed project structure.

## Project Structure

The project is divided into two main components:

-   `frontend/`: Contains the frontend Flask applicatio that serves the main HTML page.
-   `backend/`: Contains the backend Flask application that provides the API endpoints for managing blog posts.

## API Definition

The API is defined using the OpenAPI 3.0 specification. The definition can be found in the following file:

```
backend/static/swagger.json
```

## Running the API

To run the backend API server, follow these steps:

1.  Navigate to the project's root directory.
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Start the backend server:
    ```bash
    python backend/backend_app.py
    ```
The server will start on `http://localhost:5002`.

## Exploring the API

Once the backend server is running, you can explore and interact with the API in two ways:

### 1. Swagger UI (Recommended)

Navigate to the following URL in your web browser:

[http://localhost:5002/api/docs/](http://localhost:5002/api/docs/)

This will open the Swagger UI, which provides a user-friendly interface for viewing the API documentation and sending requests to the different endpoints.

### 2. Postman

As suggested in the original exercise, you can also use a tool like Postman to send requests to the API endpoints. You can import the OpenAPI definition from `backend/static/swagger.json` into Postman to automatically create a collection of requests.
