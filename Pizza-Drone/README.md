# Pizza Drone challenge.

FastAPI backend service simulating a pizza delivering drone. Can integrate either Postgres database or CSV file for filtering orders to be sent to drone. Includes ML package [mlrose-hiive](https://pypi.org/project/mlrose-hiive/) to provide the optimal route based on the **Traveling Salesman Problem**.

## First

Install dependencies from "requirements.txt" file in "app" directory.
Must build docker containers before running: Enter - `docker compose up -d` from root directory.
Once containers are built and running, open a browser to http://localhost:8000 to initialize database migrations.

## How to run program:

Upon initializing database migrations, cd into "app" directory and enter - `python3 run_api.py` or `python run_api.py` if running on Windows OS.
