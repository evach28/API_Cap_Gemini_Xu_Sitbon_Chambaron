from pymongo import MongoClient, ASCENDING
# Import the logging module for configuring and using logging
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='mongodb_logs.txt', filemode='a')

# Create a logger for the 'pymongo' namespace
logger = logging.getLogger('pymongo')
logger.setLevel(logging.DEBUG)

# Create a file handler to write log messages to the 'mongodb_logs.txt' file
file_handler = logging.FileHandler('mongodb_logs.txt')
logger.addHandler(file_handler)

# Get the root logger and add the file handler to it as well
root_logger = logging.getLogger()
root_logger.addHandler(file_handler)

# Try to establish a connection to the MongoDB server
try:
    # Create a MongoClient instance with the connection URL
    conn = MongoClient("mongodb://localhost:27017/capgemini_db")

    # Check if the connection is successful
    conn.server_info()

    # Log a success message if the connection is established
    logging.info("Successfully connected to MongoDB.")

# Handle any exceptions that may occur during the connection attempt
except Exception as e:
    # Log an error message with details of the exception
    logging.error(f"Error connecting to MongoDB: {e}")

