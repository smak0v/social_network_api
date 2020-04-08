import json
import logging
import random

import constants
import requests
from requests.exceptions import ConnectionError


def set_headers(token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    return headers


def reset_headers():
    return {
        'Content-Type': 'application/json',
    }


def read_config_file():
    try:
        with open(constants.CONFIG_FILENAME) as json_file:
            config_data = json.loads(json_file.read())

        logging.info('Config data loaded successfully!')

        return config_data
    except FileNotFoundError:
        logging.info('File with config data not found!')
        exit(1)


def signup_user(count):
    user = {
        'username': 'test_user_' + str(count + 1),
        'email': 'test_user_' + str(count + 1) + '@gmail.com',
        'password1': constants.USER_PASSWORD,
        'password2': constants.USER_PASSWORD,
        'first_name': 'Test',
        'last_name': 'User',
    }
    response = None

    try:
        response = requests.post(constants.ENDPOINT + 'users/signup/', data=json.dumps(user), headers=reset_headers())
    except ConnectionError:
        logging.error('Server is not available!')
        exit(1)

    logging.info('User ' + user['username'] + ' registered successfully!')

    return response.json()['tokens']['access']


def create_posts(configs, access_token):
    posts_count_for_creating = random.randint(0, configs.get('max_posts_per_user', constants.MAX_POSTS_PER_USER))

    for j in range(posts_count_for_creating):
        post = {
            'title': 'Post ' + str(constants.POSTS_COUNT + j + 1),
            'description': 'Post description ' + str(constants.POSTS_COUNT + j + 1),
            'content': 'Post content ' + str(constants.POSTS_COUNT + j + 1),
        }
        response = None

        try:
            response = requests.post(constants.ENDPOINT + 'posts/', data=json.dumps(post),
                                     headers=set_headers(access_token))
        except ConnectionError:
            logging.error('Server is not available!')
            exit(1)

        constants.POSTS_COUNT += posts_count_for_creating

        logging.info('Post ' + str(response.json()['id']) + ' created successfully!')


def like_posts(configs, access_token, posts):
    for _ in range(configs.get('max_likes_per_user', constants.MAX_LIKES_PER_USER)):
        post_index = random.randint(0, len(posts) - 1)

        try:
            response = requests.post(constants.ENDPOINT + 'posts/like/' + str(posts[post_index]['id']) + '/',
                                     headers=set_headers(access_token))
        except ConnectionError:
            logging.error('Server is not available!')
            exit(1)

        logging.info('Post ' + str(posts[post_index]['id']) + ' liked successfully!')


def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')

    access_tokens = []
    posts_response = None
    config_data = read_config_file()

    if config_data:
        for i in range(config_data.get('number_of_users', constants.NUMBER_OF_USERS)):
            access_token = signup_user(i)
            access_tokens.append(access_token)
            create_posts(config_data, access_token)

        try:
            posts_response = requests.get(constants.ENDPOINT + 'posts/', headers=reset_headers())
        except ConnectionError:
            logging.error('Server is not available!')
            exit(1)

        for access_token in access_tokens:
            like_posts(config_data, access_token, posts_response.json())

        logging.info('Automated bot worked successfully!')
    else:
        logging.error('No configuration data in file!')


if __name__ == "__main__":
    main()
