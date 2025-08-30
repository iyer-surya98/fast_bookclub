# Fast Bookclub

A Goodreads-style web application built with FastAPI, Beanie (MongoDB ODM), and FastAPI Users. Users can register, log in, save books as favourites or "want to read", add book reviews, participate in discussions, and search/add books using the Google Books API.

## Features

- User authentication (JWT)
- Register, login, password reset, email verification
- Save books as favourites or "want to read"
- Add and manage book reviews
- Participate in book discussions
- Search and add books via Google Books API

## Tech Stack

- [**FastAPI**](https://fastapi.tiangolo.com/)
- **MongoDB**
- [**Beanie**](https://github.com/BeanieODM/beanie): MongoDB ODM
- [**FastAPI Users**](https://fastapi-users.github.io/fastapi-users/latest/): Authentication & user management
- [**uv**]((https://github.com/astral-sh/uv)): Python package manager & runner
- [**Google Books API**](https://developers.google.com/books/docs/overview): For searching and adding books

## Getting Started

### Prerequisites

- Python 3.11
- MongoDB running locally or remotely
- [`uv`](https://github.com/astral-sh/uv) is optional but highly recommended

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/iyer-surya98/fast-bookclub.git
    cd fast-bookclub
    ```
2. If you're using `uv`, running the following command will automatically create a virtual environment and install the required packages:
    ```sh
    uv sync
    ```
    Alternatively, if you're using `pip`, you can create a virtual environment first:
    ```sh
    python -m venv .venv
    ```
    Then you can run the following commands to activate the virtual environment and install the required packages there. 
    ```sh
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Set up environment variables in .env:
    ```
    DATABASE_URL="mongodb://localhost:27017"
    DATABASE_NAME="your_database_name"
    SECRET="your_secret_key"
    JWT_LIFETIME_SECONDS=3600
    GOOGLE_BOOKS_API_KEY="your_google_books_api_key"
    ```
    For instructions on how to generate an API Key, refer to [Google Books API guide](https://developers.google.com/books/docs/v1/using#APIKey).

### Running the App

Start the server using uv:
```sh
uv run uvicorn main:app --reload
```
Alternatively:
```sh
python main.py
```