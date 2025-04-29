# FastAPI Blog API

This is a simple blog API built using FastAPI. It supports various endpoints for fetching and creating blog posts. The API also demonstrates how to create endpoints that handle different HTTP methods, including GET and POST.

## Features

- **GET `/`**: Returns a message with a list of blogs.
- **POST `/blog`**: Allows creating a new blog by sending a request with blog title, body, and optional published status.
- **GET `/blog/{id}`**: Fetches a blog by its unique ID.
- **GET `/blog/unpublished`**: Retrieves a list of unpublished blogs.
- **GET `/blog/{id}/comments`**: Fetches the comments associated with a specific blog.
  
## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI server to run FastAPI applications.
- **Optional Parameters**: Use of Python's `Optional` from `typing` to make fields optional.

## Setup

To get started with this project, you'll need Python installed on your machine. If you don't have it installed, you can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

First, clone the repository (if applicable) or create a directory for your project.

Install the required dependencies using `pip`:

```bash
pip install fastapi uvicorn
