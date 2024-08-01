#!/bin/bash

# Update package lists
apt-get update

# Install curl and ODBC dependencies
apt-get install -y curl apt-transport-https

# Add Microsoft package signing key
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add Microsoft SQL Server repository
curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update package lists after adding new repository
apt-get update

# Install ODBC driver for SQL Server
ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Install unixodbc-dev for pyodbc
apt-get install -y unixodbc-dev

# Start the Gunicorn server
gunicorn -w 3 app:app
