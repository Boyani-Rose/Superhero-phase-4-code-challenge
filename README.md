# Superhero-phase-4-code-challenge

Here is your updated **README** file without any emojis:

---

# Superheroes API

## Description

The **Superheroes API** is a Flask-based RESTful API designed to manage heroes, their powers, and the strength of each hero-power relationship. This backend service allows clients to retrieve, update, and assign powers to various superheroes, making it a great foundation for a superhero-themed app or educational demo project.

## Project Owner

**Name:** Rose Boyani

## Features

* Get a list of all heroes
* View details for a specific hero, including their powers
* List all powers
* View details for a specific power
* Update a power’s description (with validation)
* Assign a power to a hero using strength levels ("Strong", "Weak", "Average")

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/superheroes-api.git
   cd superheroes-api
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   pipenv install && pipenv shell
   ```

3. **Install dependencies:**

   ```bash
   pipenv install && pipenv shell  ```

4. **Set up the database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Seed the database:**

   ```bash
   python seed.py
   ```

6. **Run the app:**

   ```bash
   flask run
   ```

   The app will run on: `http://localhost:5555`

## API Endpoints

| Method | Endpoint       | Description                              |
| ------ | -------------- | ---------------------------------------- |
| GET    | `/heroes`      | Get list of all heroes                   |
| GET    | `/heroes/<id>` | Get detailed info on a specific hero     |
| GET    | `/powers`      | List all powers                          |
| GET    | `/powers/<id>` | View details of a specific power         |
| PATCH  | `/powers/<id>` | Update a power’s description             |
| POST   | `/hero_powers` | Assign a power to a hero (with strength) |

## Data Validation

* `PATCH /powers/:id`: Description must be 20+ characters
* `POST /hero_powers`: Strength must be one of: `"Strong"`, `"Weak"`, or `"Average"`

## Support / Contact

If you encounter any issues or have suggestions, feel free to reach out:

Email: [rosebmomamnyi@gmail.com]
GitHub: [github.com/Boyani-Rose]

