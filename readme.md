# Project Name

## Installation Guide

Follow these steps to set up the project in a virtual environment using `.venv`.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Steps

1. **Clone the repository:**
  - HTTPS
  ```sh
  git clone https://github.com/aufasyaihan/flask-crud.git
  cd flask-crud
  ```
  - SSH
  ```sh
  git clone git@github.com:aufasyaihan/flask-crud.git
  cd flask-crud
  ```

2. **Create a virtual environment:**
  ```sh
  python -m venv .venv
  ```

3. **Activate the virtual environment:**

  - On Windows:
    ```sh
    .\.venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```sh
    source .venv/bin/activate
    ```

4. **Install the required packages:**
  ```sh
  pip install -r requirements.txt
  ```

5. **Run the application:**
  ```sh
  python app.py
  ```

### Deactivating the Virtual Environment

To deactivate the virtual environment, simply run:
```sh
deactivate
```

### Additional Notes

- If you encounter any issues, please refer to the [Flask documentation](https://flask.palletsprojects.com/) for further assistance.
