import aiohttp
import asyncio

async def get_tweets_route_1():
    url = 'http://127.0.0.1:5000/get_tweets'
    
    json_data = {
        "user": "elonmusk"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Get Tweets #1: {response}")

async def get_tweets_route_2():
    url = 'http://127.0.0.1:5000/get_tweets'
    
    json_data = {
        "id": 44196397
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Get Tweets #2: {response}")

async def search_user_route():
    url = 'http://127.0.0.1:5000/search_user'
    
    json_data = {
        "user": "elonmusk"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Search User: {response}")

async def get_tweet_route():
    url = 'http://127.0.0.1:5000/get_tweet'
    
    json_data = {
        "tweet_id": 1759857255124807757
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Get Tweet: {response}")

async def like_tweet_route():
    url = 'http://127.0.0.1:5000/like_tweet'
    
    json_data = {
        "email": "elijahn9fal@gmx.com",
        "tweet_id": 1759857255124807757
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Like Tweet: {response}")

async def reply_tweet_route():
    url = 'http://127.0.0.1:5000/reply_tweet'
    
    json_data = {
        "email": "elijahn9fal@gmx.com",
        "content": "This is a tweet reply.",
        "tweet_id": 1759857255124807757
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Reply Tweet: {response}")

async def quote_tweet_route():
    url = 'http://127.0.0.1:5000/quote_tweet'
    
    json_data = {
        "email": "elijahn9fal@gmx.com",
        "content": "This is a tweet quote.",
        "tweet_id": 1759857255124807757
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Quote Tweet: {response}")

async def retweet_route():
    url = 'http://127.0.0.1:5000/retweet'
    
    json_data = {
        "email": "elijahn9fal@gmx.com",
        "tweet_id": 1759857255124807757
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as response:
            
            response = await response.text()
            print(f"Retweet Tweet: {response}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_tweets_route_1())
    loop.run_until_complete(get_tweets_route_2())
    loop.run_until_complete(search_user_route())
    loop.run_until_complete(get_tweet_route())
    loop.run_until_complete(like_tweet_route())
    loop.run_until_complete(reply_tweet_route())
    loop.run_until_complete(quote_tweet_route())
    loop.run_until_complete(retweet_route())
