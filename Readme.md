# Cool Travel API

This project helps users discover the coolest travel destinations in Bangladesh and decide whether they should travel to a specific destination based on the weather forecast.

## Features

- **Coolest 10 Districts**: Get a list of the 10 coolest districts based on the average temperature at 2 PM for the next 7 days.
- **Travel Decision**: Compare the temperature of two locations at 2 PM on a specific date and decide whether it's a good idea to travel.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.9 or higher**
- **Git** (for cloning the repository)

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/AshfaqJamil/cool-travel.git
cd cool-travel
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

This project uses SQLite by default. If you want to use PostgreSQL, update the `DATABASES` setting in `cool_travel/settings.py` with your database credentials.

Apply database migrations:
```bash
python manage.py migrate
```

### 5. Load District Data

The project includes a custom management command to load district data into the database:
```bash
python manage.py load_districts
```

This command fetches district data from a JSON file and stores it in the database.

### 6. Fetch and Store Weather Data

The project includes another custom management command to fetch weather data for all districts:
```bash
python manage.py load_weather_data
```

This command uses the Open-Meteo API to fetch weather forecasts for the next 7 days and stores the data in the database.

### 7. Run the Development Server

Start the Django development server:
```bash
python manage.py runserver
```

### 8. Access the API

- Coolest 10 Districts: http://localhost:8000/api/coolest-districts/
- Travel Decision: http://localhost:8000/api/travel-decision/?source=Dhaka&destination=Rangamati&date=2025-02-01

## API Endpoints

### 1. Coolest 10 Districts

- **URL**: `/api/coolest-districts/`
- **Method**: GET
- **Description**: Returns the 10 coolest districts based on the average temperature at 2 PM for the next 7 days.

### 2. Travel Decision

- **URL**: `/api/travel-decision/`
- **Method**: GET
- **Parameters**:
  - `source`: The name of the source district
  - `destination`: The name of the destination district
  - `date`: The date of travel in YYYY-MM-DD format
- **Description**: Compares the temperature of the source and destination districts at 2 PM on the specified date and returns a decision on whether to travel.

## Management Commands

The project includes two custom management commands to simplify data loading and fetching:

### 1. load_districts

- **Purpose**: Loads district data into the database
- **Usage**:
  ```bash
  python manage.py load_districts
  ```
- **Details**: This command reads district data from a JSON file and stores it in the District model.

### 2. load_weather_data

- **Purpose**: Fetches weather data for all districts and stores it in the database
- **Usage**:
  ```bash
  python manage.py load_weather_data
  ```
- **Details**: This command uses the Open-Meteo API to fetch weather forecasts for the next 7 days and stores the data in the WeatherData model.

## Project Structure

```
cool-travel/
├── cool_travel/               # Django project settings
├── travel/                    # Main app
│   ├── management/commands/   # Custom management commands
│   ├── migrations/           # Database migrations
│   ├── models.py             # Database models
│   ├── views.py              # API views
│   ├── urls.py               # App URLs
│   └── utils.py             # Utility functions
├── .gitignore                # Git ignore file
├── manage.py                 # Django management script
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```
