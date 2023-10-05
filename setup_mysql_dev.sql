-- Check if the database hbnb_dev_db already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a user hbnb_dev with the password hbnb_dev_pwd in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
