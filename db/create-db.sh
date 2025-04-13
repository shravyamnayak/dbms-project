docker run --name doctors_appointment_mysql \
    -e MYSQL_ROOT_PASSWORD=root_password \
    -e MYSQL_DATABASE=doctors_appointment \
    -e MYSQL_USER=admin \
    -e MYSQL_PASSWORD=asdfghjkl \
    -p 3306:3306 \
    -d mysql:8.0
