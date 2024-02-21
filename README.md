# Twitter Flask API

## Getting Started
To get started, simply put all accounts in the `accounts.txt` file in the format of `login:pass:email:emailpass`. If it is not in this format, it will be ignored.

The next thing you need to do is install the required libraries. You can use the command `pip instal -r requirements.txt` and it will automatically handle the rest!

Next, run the main.py file and yoiu should see all the accounts get created or give you a warning that they already exist. The API will run on port 5000, this can be changed on the very bottom line of the file if needed.

You are now able to run the tests to make sure everything is working as expected. You will not be able to use the same instance of python for the tests, so open up a command prompt/terminal, `cd` into the folder, and run `python3 tests.py`.

## Usage
You will find all the endpoint usages here along with their expected responses.

`get_tweets`
```curl
curl -X POST http://127.0.0.1:5000/get_tweets \
-H "Content-Type: application/json" \
-d '{"user": "elonmusk"}'
```
Response: ```json
[
  {
    "id": "1234567890",
    "url": "https://twitter.com/elonmusk/status/1234567890",
    "content": "Just launched a car into space",
    "likes": 420000,
    "views": 1000000,
    "username": "elonmusk",
    "displayName": "Elon Musk",
    "avatar": "https://example.com/avatar.jpg",
    "followers": 50000000,
    "friends": 100,
    "verified": true
  }
]
```
