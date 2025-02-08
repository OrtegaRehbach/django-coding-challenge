# Django Coding Challenge

## The Goal

Imagine this application is part of an online store. Your task is to create API endpoints to manage products and process orders. Your implementation should ensure that orders cannot be placed for products that don’t exist or are out of stock. This will give you hands-on experience with building real-world APIs. This challenge is designed to test how well you learn and adapt. You don’t need to have prior experience with Django, Docker, or Svelte but you should be comfortable figuring things out on your own. Use official documentation, Google, and AI tools to find solutions.

## Problem Statement

Your company has a Django application that stores product information. Each product has a name, price, and quantity available. Your task is to create three API endpoints:

1. `GET /api/products/`: This endpoint should return a list of all products, with each product's name, price, and quantity available.

2. `POST /api/order/`: This endpoint should accept a list of products and quantities, calculate the total cost of the order, and return it. If a product doesn't exist or there isn't enough quantity available, it should return an appropriate error message.

3. `PUT /api/products/<id>/` or `PATCH /api/products/<id>/`: These endpoints should allow for editing the details of a product. The `PUT` method should update all fields of the product, while the `PATCH` method should allow partial updates.

You can search globally for `TODO` to find the files you must edit to complete this assignment.


## General Project Introduction

This challenge involves working with a Django backend and a Svelte frontend. You will implement API endpoints to manage product data, create orders, and update product information. These endpoints will be used by a simple Svelte UI (already built) to help you visualize your work. The challenge is designed to test your ability to learn and adapt to new technologies. It is very important that you communicate well, so please don't hesitate to reach out for help in _any_ step along the way. 

- The Django part of the code, where you will be focusing the most is located in the `nimblestore/checkout` folder. Here you'll find a project already setup that's designed to use Django Rest Framework. 
- The Frontend part of the code is located in the `nimblestore/nimblestore_ui` folder, you may notice under this location most files are either `.js` or `.svelte` files for that reason.

### Django & Django REST Framework

Django is a very _opinionated_ framework, but it is also very easy to understand and to customize. If this is your first time working with Django I would suggest you first follow the tutorial at their official documentation (https://docs.djangoproject.com/en/5.1/intro/tutorial01/) The most important concepts yuo should aim to grasp are *Models*, *Views* and *Migrations*.

Enter Django REST Framework (DRF):

REST is a communication standard, you can read the technical definition here https://www.redhat.com/en/topics/api/what-is-a-rest-api, but in simple terms, REST is just a way of communicating data between applications using HTTP requests.

Fortunately for us, DRF brings a lot of tools that will help us conform to the REST rules and standards, we just have to learn how to use those tools.

### Svelte

The svelte app is very simple, you don't really have to do anything to it unless you want to improve a bit of how it looks. You should however, try and understand how it works. Most of the heavy lifting is being done by the components used in `App.svelte` file.

### Docker

Docker allows us to package all dependencies and configurations so that your development environment is identical to production. This means you don’t need to manually install PostgreSQL, Python, or Node.js on your computer. Everything runs inside containers. If you've never used Docker or containers before I definitely recommend you to readn the [What is Docker?](https://docs.docker.com/get-started/docker-overview/) article from their documentation. You don't have to read the article to complete this challenge, it is always a good practice to know the _hows_ behind the tools we learn to use.

## Setup

Here’s a more structured and beginner-friendly **Setup** section with clear steps:

---

## **Setup**

As mentioned before, this project is built using **Django** for the backend and **Svelte** for a minimal frontend interface. To simplify setup and ensure a consistent environment, we use **Docker** to run the application.

### **1. Install Prerequisites**
Before getting started, you need to install the following on your system:
- **[Python](https://www.python.org/downloads/)**
- **[Docker](https://docs.docker.com/get-docker/)**
- **[Docker Compose](https://docs.docker.com/compose/install/)** (included with Docker Desktop on Windows & Mac)

If you're new to Docker, refer to the **Installation Help** section below.

### **2. Clone the Repository**
Open a terminal and clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>
```
If you're using **GitHub Desktop** or **VS Code**, you can also clone the repository using their built-in Git features.

### **3. Start the Application**
Run the following command to **build and start** the project:
```bash
docker compose up --build
```
This will:
- Pull necessary Docker images.
- Install dependencies.
- Start all required services.

### **4. Run Migrations**
Once the containers are up, you need to set up the database:
```bash
docker compose exec django bash  # Open a shell inside the Django container
python manage.py migrate         # Apply database migrations
```
If successful, you should see a new **`db.sqlite3`** file in your project directory.

### **5. Open the Application**
After completing the steps above, open your browser and go to:
[https://127.0.0.1:8080](https://127.0.0.1:8080)

- This page provides a simple UI to test the API.
- Open **Web Inspector** (F12) → **Network Tab** to see API requests in action.
- The frontend is already set up for you; you **do not need to modify it**.

### **6. Development Workflow**
When you start building your solution, you will need to create models and apply migrations:
```bash
docker compose exec django bash  # Open a shell inside the running container
python manage.py makemigrations  # Detect model changes
python manage.py migrate         # Apply database migrations
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

Pre-commit hooks help ensure that your code follows best practices before it is committed to the repository. It automatically formats your code and checks for common errors. This saves time by catching issues early.

- **Pre-commit**: Install `pre-commit` to ensure code quality before commits. Pre-commit hooks can automatically format your code and run tests before each commit. `pre-commit` must be installed by running the following commands:
  Initialize the pre-commit hooks with:
  ```bash
  pip install pre-commit
  pre-commit install
  ```
  Now, every time you make a commit, `pre-commit` will run the defined hooks to ensure code quality.

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
docker compose --version
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


# Additional Resources

- **Official Docker Compose Documentation**: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- **Docker CLI Reference**: [https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)


Good Luck,
Juan Mora
