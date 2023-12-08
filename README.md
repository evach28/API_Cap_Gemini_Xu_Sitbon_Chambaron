# FastAPI MongoDB REST API

## Introduction

This project is a RESTful API built using FastAPI for creating, reading, updating, and deleting data in a MongoDB database. It provides an interface to interact with stock information about french companies unsing the siret number as the research criteria. It can be useful to find any company sing the siret number, it provides basic information such as the name, the adress, the activity of the company and other informations. 

This API project is part of the Big Data Applications course given by Capgemini. The development team consists of Eva CHAMBARON, Rahamim SITBON, and Joseph XU. We used the tool fastAPI as an application ressource and mongoDB as a local database. We decided to use fastAPI because this tool provided an easy build of the API whith optimal performances. 

We faced some difficulties related to the database because the dataset is very heavy and most of the tools can't support that amount of data. We decided to put our dataset in a local MongoDB database, which we connected to our code to query the informations. 

## Folder structure 
The config folder contains a db.py file, which is the configuration file to connect the database to the project. 

The models folder contains a stock.py file which defines the structure of the data model. Each columns has a specified type and this is where we are making sure that all the columns are well defined and are well used. 

The routes folder contains the stock.py file which defines the FastAPI functions. The functionnality HTTP GET and DELETE are defined in this file. 

The schemas folder contains the stock.py file which contains two functions which are used in the context of transforming data before returning it from an API endpoint or before storing it in a database. 

The .gitignore file is used by Git to etermine which files and directories should be ignored and not tracked by version control.
The index.py sets the FastAPI application and includes the router named 'stock'. 
The mongodb_logs.txt is the log file where we can find the different actions. 
The requirements.txt defines the different dependencies needed to run the project. 

## Setup Environment

1. Create a virtual environment using [virtualenv](https://pypi.org/project/virtualenv/):

    ```bash 
    virtualenv venv
    ```

2. Activate the virtual environment:

    - For Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

    - For Windows:

        ```bash
        source venv/Scripts/activate
        ```

## Install Dependencies

Install the required packages using pip (You can find all dependencies in our requirements.txt file):

```bash
pip install fastapi pymongo uvicorn
```

## Create the local database

Open the MongoDB Compass application. Create a new database named "capgemini_db" and a collection named "capgemini_clt". Then click on the import data button and select the file "StockEtablissement_utf8" then click on import. Then copy the connection string and paste it in the db.py file on "conn" line. 

## Start the Server

Run the FastAPI application using uvicorn:

```bash
uvicorn index:app --reload
```
The --reload option enables automatic reloading of the server on code changes, making development easier.

## API Endpoints
```bash
GET /{siret}: Retrieve information for a specific stock based on its SIRET number.
```
```bash
DELETE /{siret}: Delete a stock entry based on its SIRET number.
```
## Usage
Access the API documentation at http://127.0.0.1:8000/docs for interactive documentation.

Use http://127.0.0.1:8000/redoc for a more structured API documentation.

## Sources 
We used generative IA to do the log code and to correct some errors that occured when we coded. The rest of the code is from other sources such as videos and stack overflow.
