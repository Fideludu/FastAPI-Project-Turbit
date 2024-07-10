# My Project

## Overview
This project sets up a MongoDB database using Docker Compose, retrieves data from an external API, and exposes this data through a FastAPI application.

## Setup

1. Start MongoDB with Docker Compose:
    ```sh
    docker-compose up -d
    ```

2. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Load data into MongoDB:
    ```sh
    python data/load_data.py
    ```

4. Run the FastAPI application:
    ```sh
    uvicorn app.main:app --reload
    ```

## Endpoints

- `/user_posts_count`: Get the total number of posts from each user.
- `/post_comments/{post_id}`: Get comments for a specific post.
- `/users`: Add a new user.
- `/users/{user_id}`: Modify an existing user.
- `/users/{user_id}`: Delete a user.

## Running Tests

Run the tests using pytest:
```sh
pytest tests/
