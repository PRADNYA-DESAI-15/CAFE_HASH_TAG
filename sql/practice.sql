CREATE DATABASE pet_store;

CREATE USER 'pet_user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON pet_store.* TO 'pet_user'@'localhost';

FLUSH PRIVILEGES;
