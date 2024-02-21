# Twitter Flask API

## Getting Started
To get started, simply put all accounts in the `accounts.txt` file in the format of `login:pass:email:emailpass`. If it is not in this format, it will be ignored.

The next thing you need to do is install the required libraries. You can use the command `pip instal -r requirements.txt` and it will automatically handle the rest!

Next, run the main.py file and yoiu should see all the accounts get created or give you a warning that they already exist. The API will run on port 5000, this can be changed on the very bottom line of the file if needed.

You are now able to run the tests to make sure everything is working as expected. You will not be able to use the same instance of python for the tests, so open up a command prompt/terminal, `cd` into the folder, and run `python3 tests.py`.

## Usage
You will find all the endpoint usages here along with their expected responses.

### `get_tweets`
`get_tweets` takes either a "user" or "id".

```curl
curl -X POST http://127.0.0.1:5000/get_tweets \
-H "Content-Type: application/json" \
-d '{"user": "elonmusk"}'
```

Expected Response:
```json
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

```curl
curl -X POST http://127.0.0.1:5000/get_tweets \
-H "Content-Type: application/json" \
-d '{"id": 44196397}'
```

Expected Response:
```json
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

### `search_user`
`search_user` takes a `user`.

```curl
curl -X POST http://127.0.0.1:5000/search_user \
-H "Content-Type: application/json" \
-d '{"user": "elonmusk"}'
```

Expected Response:
```json
{
   "displayName":"Elon Musk",
   "followers":173302871,
   "friends":542,
   "id":44196397,
   "url":"https://twitter.com/elonmusk",
   "username":"elonmusk",
   "verified":true
}
```

### `get_tweet`
`get_tweet` takes a `tweet_id`,

```curl
curl -X POST http://127.0.0.1:5000/get_tweet \
-H "Content-Type: application/json" \
-d '{"tweet_id": 1234567890}'
```

Expected Response:
```json
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

### `like_tweet`
`like_tweet` takes `email` and `tweet_id`.

```curl
curl -X POST http://127.0.0.1:5000/like_tweet \
-H "Content-Type: application/json" \
-d '{"email": "example@example.com", "tweet_id": 1234567890}'
```

Expected Response:
`True`

### `reply_tweet`
`reply_tweet` takes `email`, `content`, and `tweet_id`.

```curl
curl -X POST http://127.0.0.1:5000/reply_tweet \
-H "Content-Type: application/json" \
-d '{"email": "example@example.com", "content": "This is a tweet reply.", "tweet_id": 1234567890}'
```

Expected Response:
`True`

### `quote_tweet`
`quote_tweet` takes `email`, `content`, and `tweet_id`.

```curl
curl -X POST http://127.0.0.1:5000/quote_tweet \
-H "Content-Type: application/json" \
-d '{"email": "example@example.com", "content": "This is a tweet quote.", "tweet_id": 1234567890}'
```

Expected Response:
`True`

### `retweet_tweet`
`quote_tweet` takes `email` and `tweet_id`.

```curl
curl -X POST http://127.0.0.1:5000/retweet \
-H "Content-Type: application/json" \
-d '{"email": "example@example.com", "tweet_id": 1234567890}'
```

Expected Response:
`True`

## Contact
Feel free to contact `someone0171` on Discord for support up to 3 months! Support starts on 2/25/24 (February 25th, 2024) and ends 5/25/24 (May 25th, 2024.).
