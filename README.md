# ChatDB

ChatDB is a natural language interface for interacting with a MySQL database.  It allows users to query the database using natural language, which is then translated into SQL.

## Files

* `config.py`:  Contains configuration settings for the MySQL database connection and the OpenAI API key.
* `main.py`:  The main entry point of the application. It parses the user's natural language query, translates it to SQL, executes the SQL query against the database, and displays the results.
* `mysql_client.py`:  Handles the connection to the MySQL database.
* `openai_client.py`:  Handles the connection to the OpenAI API for translating natural language to SQL.
* `translator.py`:  Contains the logic for translating the natural language query to SQL using the OpenAI API.

## Setup and Installation

### Prerequisites

* Python 3.6 or higher
* MySQL Database
* OpenAI API Key

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd ChatDB
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install mysql-connector-python openai
    ```

3.  **Configure the `config.py` file:**

    * Set the OpenAI API key:

        ```python
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "API_KEY_GOES_HERE")
        ```
        Replace `API_KEY_GOES_HERE` with your actual OpenAI API key or set it as an environment variable.

    * Configure the MySQL database connection settings:

        ```python
        MYSQL_HOST = "your_mysql_host"
        MYSQL_PORT = your_mysql_port
        MYSQL_USER = "your_mysql_user"
        MYSQL_PASSWORD = "your_mysql_password"
        MYSQL_DATABASE = "your_mysql_database"
        ```

        **Note:** Ensure your MySQL server is running and accessible.  You'll need a database named `chatdb` and a user with appropriate permissions.  The default password is an empty string, which should be changed in both the database and code before running to ensure data security.

4.  **Database Setup**

    * The code is designed to work with a database containing the following schema:

        ```
        Tables:
          runners(runner_id INT PK, name VARCHAR, age TINYINT)
          races(race_id INT PK, name VARCHAR, date DATE, location VARCHAR, distance_km DECIMAL)
          race_results(result_id INT PK, runner_id INT FK→runners, race_id INT FK→races,
                       bib_number VARCHAR, finish_time_sec INT, finish_rank INT)
        ```
    * You'll need to create these tables in your `chatdb` database.  Here's some SQL statements to create the necessary tables:

        ```sql
        CREATE TABLE runners (
            runner_id INT PRIMARY KEY,
            name VARCHAR(255),
            age TINYINT
        );

        CREATE TABLE races (
            race_id INT PRIMARY KEY,
            name VARCHAR(255),
            date DATE,
            location VARCHAR(255),
            distance_km DECIMAL
        );

        CREATE TABLE race_results (
            result_id INT PRIMARY KEY,
            runner_id INT,
            race_id INT,
            bib_number VARCHAR(20),
            finish_time_sec INT,
            finish_rank INT,
            FOREIGN KEY (runner_id) REFERENCES runners(runner_id),
            FOREIGN KEY (race_id) REFERENCES races(race_id)
        );
        ```

## Usage

To run ChatDB, execute the `main.py` script from the command line, providing your natural language query as an argument.

```bash
python main.py -q "Which runner finished first in the 'San Francisco Marathon'?"
