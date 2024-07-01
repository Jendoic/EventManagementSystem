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

- **List all events**: `GET api/v1/ems/events/`
- **Create a new event**: `POST api/v1/ems /events/`
- **Retrieve an event**: `GET  api/v1/ems/events/{id}/`
- **Update an event**: `PUT  api/v1/ems/events/{id}/`
- **Delete an event**: `DELETE  api/v1/ems/events/{id}/`



### RSVP Endpoints

- **List all RSVPs**: `GET api/v1/ems/rsvps/`
- **Create a new RSVP**: `POST api/v1/ems /rsvps/`
- **Retrieve an RSVP**: `GET api/v1/ems/rsvps/{id}/`
- **Update an RSVP**: `PUT api/v1/ems/rsvps/{id}/`
- **Delete an RSVP**: `DELETE api/v1/ems/rsvps/{id}/`

### Notification Endpoints

- **List all notifications**: `GET api/v1/ems/notifications/`
- **Retrieve a notification**: `GET api/v1/ems/notifications/{id}/`
- **Delete a notification**: `DELETE api/v1/ems/notifications/{id}/`

### Category Endpoints

- **List all categories**: `GET  api/v1/ems/categories/`
- **Create a new category**: `POST api/v1/ems/categories/`
- **Retrieve a category**: `GET /categories/{id}/`
- **Update a category**: `PUT api/v1/ems/categories/{id}/`
- **Delete a category**: `DELETE api/v1/ems/categories/{id}/`

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/jendoic/event-management-system.git
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

- Access the API at `http://localhost/`.
- Use tools like Postman or cURL to interact with the API endpoints.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.



