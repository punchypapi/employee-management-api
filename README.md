# Employee Management API

## Project Overview

The Employee Management API is a FastAPI-based web application designed to manage employee data. This project aims to demonstrate the process of setting up a GitHub repository, creating a virtual environment, generating fake employee data, and developing a GET API endpoint to retrieve employee information.

## Features

- **Employee Data Generation**: Uses Python class definitions and methods to generate realistic employee data, including names, email addresses, departments, hire dates, and more.
- **API Endpoint**: Provides a GET endpoint to retrieve employee data based on employee ID.
- **Dynamic Data**: Employee data is generated dynamically using the `random` module.

## Setup and Installation

### Prerequisites

- Python 3.12 or later
- FastAPI
- Uvicorn
- Git

### Installation Steps

1. **Clone the Repository**
```sh
git clone https://github.com/your-username/employee-management-api.git  employee-management-api
```
2. **Create and Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate
```
3. **Install Dependencies**
```sh
pip install -r requirements.txt
```
4. **Run the Application Locally**
```sh
uvicorn main:app --reload --port 8001
```

## Key Files and Directories

The project directory structure is organized as follows:

- **app/**: Contains the main application modules.
  - `__init__.py`: Initializes the Python package and Creates instances of employees using generated data.
  - `data_generator.py`: Generates fake data for employees.

- **fake_data/**: Contains text files used for generating fake employee names.
  - `first-names.txt`
  - `last-names.txt`

- **main.py**: Entry point of the FastAPI application.

- **requirements.txt**: Lists the dependencies required for the project.

- **README.md**: Provides an overview and setup instructions for the project.

## Usage

### API Endpoint

#### GET `/`

Retrieve information about an employee by their ID.

**Query Parameters:**
- `employee_id` (str): The ID of the employee to retrieve.

**Response:**
- `200 OK`: Returns the employee data as a JSON object.
- `404 Not Found`: If the employee ID does not exist.

**Example Request:**

```sh
curl "http://127.0.0.1:8001/?employee_id=<employee_id>"
