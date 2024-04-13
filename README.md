
# Conference Room Booking Service

## Overview
This microservice, developed with FastAPI and Pydantic, provides a simple conference room booking system. Users can create, view, and cancel their reservations. This service uses MySQL for data persistence and is designed to be deployed on AWS Lambda using the Serverless framework.

## Features
- **Create Reservation:** Users can book a conference room by providing details such as the room name, booking name, date, and the number of people.
- **View Reservations:** Users can view all their active reservations.
- **Cancel Reservation:** Users can cancel their existing reservations.

## API Documentation
The API endpoints include:

- `POST /reservations/`: Create a new reservation.
  - Input: `{"room_name": "string", "booker_name": "string", "date": "YYYY-MM-DD", "number_of_people": int}`
  - Output: Details of the created reservation.
- `GET /reservations/`: Get all reservations.
  - Output: List of all reservations.
- `POST /reservations/by-name`: Get reservations by booker name.
  - Input: `{"booker_name": "string"}`
  - Output: List of reservations matching the booker name.
- `DELETE /reservations/{reservation_id}`: Cancel a reservation by ID.
  - Output: Confirmation of deletion.

## Local Setup
### Requirements
- Python 3.10+
- Docker and Docker Compose
- FastAPI
- SQLAlchemy
- Pydantic

### Steps to Run Locally
1. Clone the repository:
   ```
   git clone <repository-url>
   cd CodingTest
   ```
2. Start the MySQL database using Docker Compose:
   ```
   docker-compose up -d
   ```
   Access the API at: `http://localhost:8000`

## Testing
Run the unit tests inside the container using:
```
pytest test.py
```

## Deployment on AWS Lambda
### Prerequisites
- AWS CLI configured
- AWS SAM CLI

### Steps
1. Set up environment variables in `template.yml`

    ``` 
    DATABASE_HOST: ...
    DATABASE_USER: ... 
    DATABASE_PASSWORD: ...
    DATABASE_NAME: ...
    ```
2. Package the application:
   ```
   sam build
   ```
3. Deploy the application to AWS:
   ```
   sam deploy --guided
   ```

Follow the prompts to complete the deployment. Once deployed, the API will be accessible via the AWS-provided URL.
