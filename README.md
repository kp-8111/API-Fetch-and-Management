# Django Project: API Fetch and Management

This project demonstrates how to fetch data from an API, save it to a database, and display it using Django. The project is intended for developers to understand the basic workflow of API integration and data management in Django.

## Features
- Fetches state data from an external API.
- Saves the data into a SQLite database.
- Displays the fetched data on the home page.

## Project Structure
- **`manage.py`**: Django's administrative utility.
- **`settings.py`**: Contains project settings including database and installed apps.
- **`urls.py`**: Routes URLs to views.
- **`views.py`**: Contains logic for fetching data from the API and rendering it.
- **`models.py`**: Defines the database schema for storing state information.
- **`templates/home.html`**: Displays the data fetched from the API.

## Prerequisites
- Python 3.8 or above
- Django 4.2.4
- SQLite (default database)

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2. Install dependencies:
    ```bash
    pip install django
    ```

3. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000/` to see the project in action.

## API Integration
- API Endpoint: `https://apistate.pythonanywhere.com/`
- Data fetched includes:
  - State name
  - Capital

## Code Explanation
1. **Fetching Data**:
    The `requests` library is used in the `home` view to fetch data from the API.
    
2. **Saving to Database**:
    The data is saved in the `State` model, which has two fields: `name` and `capital`.

3. **Displaying Data**:
    Data from the database is passed to the template and displayed in a tabular format.

## Models
- `State` model:
    ```python
    class State(models.Model):
        name = models.CharField(max_length=100)
        capital = models.CharField(max_length=100)
    ```

## Troubleshooting
- Ensure the API endpoint is reachable.
- Verify that migrations have been applied correctly.
- Check the Django version compatibility.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.
