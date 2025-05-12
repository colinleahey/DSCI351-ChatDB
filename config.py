import os

# Open AI api
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "api-key")

# passwords/connection settings
MYSQL_HOST     = "127.0.0.1"
MYSQL_PORT     = 33306
MYSQL_USER     = "chatuser"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "chatdb"