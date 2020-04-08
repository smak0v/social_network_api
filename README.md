# STARNAVI Social Network API

## Description

Implementation of simple REST API for social network that include next features:

- user signup;
- user login;
- post creation;
- post deletion;
- post updating;
- post retrieving;
- posts list retrieving;
- post like;
- post unlike;
- JWT authentication:
    - retrieve access and refresh tokens;
    - refresh access token using refresh token;
    - verify access token;
- user activity (date and time for last login and last request);
- simple analytic for likes counting for dates in some range.

## API endpoints

- ```/api/v1/users/signup/```(POST) - signup user in system;

- ```/api/v1/users/login/``` (POST) - login user in system;

- ```/api/v1/users/token/refresh/``` (POST) - refresh user access token using refresh token;

- ```/api/v1/users/token/verify/``` (POST) - verify user access token;

- ```/api/v1/users/user_activity/<int:user_pk>/``` (GET) - get user activity (date and time for last login and last
request);

- ```/api/v1/posts/``` (GET) - retrieve list of all posts;

- ```/api/v1/posts/<int:post_pk>/``` (GET) - retrieve post by it primary key;

- ```/api/v1/posts/``` (POST) - create post;

- ```/api/v1/posts/<int:post_pk>/``` (DELETE) - delete post;

- ```/api/v1/posts/<int:post_pk>/``` (PUT) - update post;

- ```/api/v1/posts/like/<int:post_pk>/``` (POST) like or unlike post by user;

- ```/api/v1/analytics/?date_from=<date:date>&date_to<date:date>/``` (GET) - simple analytics.

## Service launching

To start the social network service you need to install Docker and Docker Compose in your system.

After this go to project root directory and run next command in your terminal or command prompt:

```
docker-compose up --build
```

Or you can start it manually. For this purpose you need to do next steps:

- go to ```app``` directory;

- create virtual environment (using ```virtualenv```, ```venv``` or something else);

- activate this virtual environment:

    ```shell script
    source venv_name/bin/activate
    ```

- install requirements with next command:

    ```shell script
    pip install -r requirements.txt
    ```

- run migrations into you database;

    ```shell script
    python manage.py migrate
    ```

- start service:

    ```shell script
    python manage.py runserver
    ```

## Automated bot

To run automated bot for testing the API, go to project root directory, after that to ```automated_bot``` directory and
run next command in your terminal or command prompt:

```shell script
python automated_bot.py
```

Please note that the service should work at this time.

## License

Collision is an open-sourced software licensed under the [MIT license](LICENSE.md).
