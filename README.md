# Event Management System

An API built with Django REST Framework to manage events and attendees. Features include event creation, RSVPs, user accounts, notifications, and event categories.

## Features

- **Event Creation**:
  - CRUD operations for events.
  - Schedule events with start and end times.
  - Categorize events for easier searching and filtering.
- **RSVPs**:
  - Manage RSVPs with statuses like Going, Not Going, and Maybe.
  - Track attendance.
- **User Accounts**:
  - User registration and authentication.
  - Profile management.
- **Notifications**:
  - Send notifications to users for events they are interested in or attending.
  - Track read/unread status of notifications.

## Endpoints

### Event Endpoints

- **List all events**: `GET /events/`
- **Create a new event**: `POST /events/`
- **Retrieve an event**: `GET /events/{id}/`
- **Update an event**: `PUT /events/{id}/`
- **Delete an event**: `DELETE /events/{id}/`

### User Endpoints

- **List all users**: `GET /users/`
- **Create a new user**: `POST /users/`
- **Retrieve a user**: `GET /users/{id}/`
- **Update a user**: `PUT /users/{id}/`
- **Delete a user**: `DELETE /users/{id}/`

### RSVP Endpoints

- **List all RSVPs**: `GET /rsvps/`
- **Create a new RSVP**: `POST /rsvps/`
- **Retrieve an RSVP**: `GET /rsvps/{id}/`
- **Update an RSVP**: `PUT /rsvps/{id}/`
- **Delete an RSVP**: `DELETE /rsvps/{id}/`

### Notification Endpoints

- **List all notifications**: `GET /notifications/`
- **Create a new notification**: `POST /notifications/`
- **Retrieve a notification**: `GET /notifications/{id}/`
- **Update a notification**: `PUT /notifications/{id}/`
- **Delete a notification**: `DELETE /notifications/{id}/`

### Category Endpoints

- **List all categories**: `GET /categories/`
- **Create a new category**: `POST /categories/`
- **Retrieve a category**: `GET /categories/{id}/`
- **Update a category**: `PUT /categories/{id}/`
- **Delete a category**: `DELETE /categories/{id}/`

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/event-management-system.git
    cd event-management-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the API at `http://127.0.0.1:8000/`.
- Use tools like Postman or cURL to interact with the API endpoints.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

---

Feel free to adjust the description to better match your specific implementation details and preferences.
