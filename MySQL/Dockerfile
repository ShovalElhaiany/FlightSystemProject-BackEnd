# Use the official image as a parent image.
FROM mysql:8.0

# Set the working directory in the container
WORKDIR /docker-entrypoint-initdb.d

# # Set environment variables
# ENV MYSQL_ROOT_PASSWORD='password'

# Copy the SQL script into the working directory
COPY init.sql ./
