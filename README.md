# ORM Workshop

N.B. This Django project is configured to log all SQL statements executed by the
ORM to the console.

## Setup

This demo uses Postgres as a database -- make sure you have Postgres running.

1. Checkout this repo:

  ```sh
  git clone https://github.com/samueljsb/workshop-orm
  cd workshop-orm
  ```

1. Create and activate virtual environment and install the requirements:

  ```sh
  python -m venv venv
  . venv/bin/activate
  python -m pip install -rrequirements.txt
  ```

1. Create the database and run the migrations:

  ```sh
  createdb workshop_orm
  python -m manage migrate
  ```


1. Populate the sample data:

  ```sh
  python -m manage populate_data
  ```
