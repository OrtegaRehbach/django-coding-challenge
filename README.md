# Django Coding Challenge

## Setup

Clone this repository using GIT. I recommend you use Github Desktop or VS Code (see point 1 in Development)

To run this project you need to install any recent version of Docker. 

Once you have Docker installed and working, you can install the project dependencies by running `docker compose up --build`. This will install everything for you, then you can run migrations with `docker compose exec django bash` and `python manage.py migrate` (make sure to run this command within the nimblestore directory). If successful you should see a new file called `db.sqlite3` in your work directory.

Lastly you should be able to run the server which will let you see a very basic webpage in https://127.0.0.1:8080 (Open this link in your browser), this page will help you test your work, I recommend you open the web inspector and switch to the network tab to see what is happening. If you want you can find the source for this page in the `nimblestore/nimblestore_ui/src/App.svelte` file. You do NOT need to edit anything on it.

## Development

Here are some general guides and also some tips:

1. Install VS Code (optional) [here](https://code.visualstudio.com/)
2. Install recommended extensions (Python, SonarLint)
3. Use Google as much as you need to, find official sources and documentations, examples and tutorials are good sources.
4. You CAN use AI, in fact I encourage you to do so.

Once you start creating models, you will need to create and run migrations, the commands you'll need are:

```bash
docker compose exec django bash
python manage.py makemigrations
python manage.py migrate
```

## Documentation

- **Docstrings**: Please provide docstrings for your functions and classes using the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). This helps others understand the purpose and usage of your code.
- **README**: Update the README file to include instructions on how to set up and run the project, as well as any other relevant information. This ensures that anyone who uses your project can easily get started.

## Unit Tests

- **Unit Tests with pytest**: Write unit tests for your code using `pytest`. Ensure you cover different scenarios, including edge cases.
  To run your tests, use the command:
  ```bash
  docker compose exec django bash
  pytest
  ```
  Create a `tests` directory in your project and add your test files there. Follow the convention of naming your test files starting with `test_`.

## Pre-commit Hooks

- **Pre-commit**: Install `pre-commit` to ensure code quality before commits. Pre-commit hooks can automatically format your code and run tests before each commit. `pre-commit` should have been installed by the previous commmands, yet you still have to run the following:
  Initialize the pre-commit hooks with:
  ```bash
  pre-commit install
  ```
  Now, every time you make a commit, `pre-commit` will run the defined hooks to ensure code quality.

## Problem Statement

Your company has a Django application that stores product information. Each product has a name, price, and quantity available. Your task is to create three API endpoints:

1. `GET /api/products/`: This endpoint should return a list of all products, with each product's name, price, and quantity available.

2. `POST /api/order/`: This endpoint should accept a list of products and quantities, calculate the total cost of the order, and return it. If a product doesn't exist or there isn't enough quantity available, it should return an appropriate error message.

3. `PUT /api/products/<id>/` or `PATCH /api/products/<id>/`: These endpoints should allow for editing the details of a product. The `PUT` method should update all fields of the product, while the `PATCH` method should allow partial updates.

You can search globally for `TODO` to find the files you must edit to complete this assignment.

# Getting Started with Docker Compose

## Introduction

Docker Compose is a tool for defining and running multi-container Docker applications. With a single command, you can start all the services defined in a `docker-compose.yml` file, making it easier to manage complex applications.

This guide will help you get started with Docker Compose, from installation to useful commands.

---

## Installation

To use Docker Compose, you need to have Docker installed on your system. Follow the official installation guide for your operating system:

- **Windows**: [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows/)
- **Mac**: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac/)
- **Linux**: [Install Docker Engine on Linux](https://docs.docker.com/engine/install/)

Docker Compose is included with Docker Desktop for Windows and Mac. For Linux, you may need to install it separately. Check the official guide: [Install Docker Compose](https://docs.docker.com/compose/install/).

Verify the installation by running:

```bash
dockercompose --version
```

# Key Concepts

- **Service**: A service is a containerized application defined in the `docker-compose.yml` file.
- **Project**: A project is a collection of services defined in a single `docker-compose.yml` file.
- **Volume**: A volume is a persistent storage mechanism for sharing data between containers or between a container and the host.

---

# Useful Docker Compose Commands

Here are the most common commands you'll use with Docker Compose:

## Starting and Stopping Services

- **Start all services**:  
  ```bash
  docker compose up
  ```
- **Start services in the background (detached mode)**:  
  ```bash 
  docker compose up -d
  ```
- **Stop all services**:  
  ```bash
  docker compose down
  ```
- **Stop and remove volumes**:  
  ```bash
  docker compose down -v
  ```
- **Restart services**:  
  ```bash
  docker compose restart
  ```
- **View logs of running services**:  
  ```bash
  docker compose logs
  ```
- **View logs of a specific service**:  
  ```bash
  docker compose logs <service-name>
  ```
- **Follow logs in real-time**:  
  ```bash
  docker compose logs -f
  ```


# Tips for Beginners

1. **Start Small**: Begin with a simple `docker-compose.yml` file and gradually add more services as you become comfortable.
2. **Use `.env` Files**: Store environment variables in a `.env` file to keep your configuration clean and secure.
3. **Leverage Volumes**: Use volumes to persist data between container restarts.
4. **Read the Logs**: Logs are your best friend when debugging issues with your services.

---

# Additional Resources

- **Official Docker Compose Documentation**: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- **Docker CLI Reference**: [https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)


Good Luck,
Juan Mora
