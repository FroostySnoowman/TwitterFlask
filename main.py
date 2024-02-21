import asyncio
from twscrape import API
from flask import Flask, request, jsonify
from twitter.account import Account

app = Flask(__name__)

api = API()

@app.route('/get_tweets', methods=['POST'])
async def get_tweets():
    if request.is_json:
        data = request.get_json()

        if data:
            response = []
            try:
                if data['user']:
                    user = await api.user_by_login(data['user'])
                    async for tweet in api.user_tweets(user.id, limit=5):
                        t = {
                            "id": tweet.id,
                            "url": tweet.url,
                            "content": tweet.rawContent,
                            "likes": tweet.likeCount,
                            "views": tweet.viewCount,
                            "username": tweet.user.username,
                            "displayName": tweet.user.displayname,
                            "avatar": tweet.user.profileImageUrl,
                            "followers": tweet.user.followersCount,
                            "friends": tweet.user.friendsCount,
                            "verified": tweet.user.blue
                        }
                        response.append(t)
                    return response
            except KeyError:
                try:
                    if data['id']:
                        async for tweet in api.user_tweets(data['id'], limit=5):
                            t = {
                                "id": tweet.id,
                                "url": tweet.url,
                                "content": tweet.rawContent,
                                "likes": tweet.likeCount,
                                "views": tweet.viewCount,
                                "username": tweet.user.username,
                                "displayName": tweet.user.displayname,
                                "avatar": tweet.user.profileImageUrl,
                                "followers": tweet.user.followersCount,
                                "friends": tweet.user.friendsCount,
                                "verified": tweet.user.blue
                            }
                            response.append(t)
                        return response
                except:
                    return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/search_user', methods=['POST'])
async def search_user():
    if request.is_json:
        data = request.get_json()

        if data:
            if data['user']:
                user = await api.user_by_login(data['user'])
                if user:
                    response = {
                        "id": user.id,
                        "url": user.url,
                        "username": user.username,
                        "displayName": user.displayname,
                        "followers": user.followersCount,
                        "friends": user.friendsCount,
                        "verified": user.blue
                    }
                    return response
                else:
                    return jsonify({"error": "User must be valid"}), 400
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/get_tweet', methods=['POST'])
async def get_tweet():
    if request.is_json:
        data = request.get_json()

        if data:
            if data['tweet_id']:
                tweet = await api.tweet_details(data['tweet_id'])
                if tweet:
                    response = {
                        "id": tweet.id,
                        "url": tweet.url,
                        "content": tweet.rawContent,
                        "likes": tweet.likeCount,
                        "views": tweet.viewCount,
                        "username": tweet.user.username,
                        "displayName": tweet.user.displayname,
                        "avatar": tweet.user.profileImageUrl,
                        "followers": tweet.user.followersCount,
                        "friends": tweet.user.friendsCount,
                        "verified": tweet.user.blue
                    }
                    return response
                else:
                    return jsonify({"error": "Tweet ID must be valid"}), 400
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/like_tweet', methods=['POST'])
async def like_tweet():
    if request.is_json:
        data = request.get_json()

        if data:
            if data['tweet_id']:
                tweet = await api.tweet_details(data['tweet_id'])
                if tweet:
                    valid_login = None
                    with open('accounts.txt', 'r') as file:
                        for line in file:
                            if data['email'] in line:
                                valid_login = line.strip()
                                break
                    if valid_login:
                        username, password, email, email_password = valid_login.split(':')
                        account = Account(email, username, password)
                        account.like(data['tweet_id'])
                        return True
                    else:
                        return jsonify({"error": "Email must be valid"}), 400
                else:
                    return jsonify({"error": "Tweet ID must be valid"}), 400
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/reply_tweet', methods=['POST'])
async def reply_tweet():
    if request.is_json:
        data = request.get_json()

        if data:
            if data['tweet_id']:
                tweet = await api.tweet_details(data['tweet_id'])
                if tweet:
                    valid_login = None
                    with open('accounts.txt', 'r') as file:
                        for line in file:
                            if data['email'] in line:
                                valid_login = line.strip()
                                break
                    if valid_login:
                        username, password, email, email_password = valid_login.split(':')
                        account = Account(email, username, password)
                        account.reply(data['content'], tweet_id=data['tweet_id'])
                        return True
                    else:
                        return jsonify({"error": "Email must be valid"}), 400
                else:
                    return jsonify({"error": "Tweet ID must be valid"}), 400
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/quote_tweet', methods=['POST'])
async def quote_tweet():
    if request.is_json:
        data = request.get_json()

        if data:
            if data['tweet_id']:
                tweet = await api.tweet_details(data['tweet_id'])
                if tweet:
                    valid_login = None
                    with open('accounts.txt', 'r') as file:
                        for line in file:
                            if data['email'] in line:
                                valid_login = line.strip()
                                break
                    if valid_login:
                        username, password, email, email_password = valid_login.split(':')
                        account = Account(email, username, password)
                        account.quote(data['content'], tweet_id=data['tweet_id'])
                        return True
                    else:
                        return jsonify({"error": "Email must be valid"}), 400
                else:
                    return jsonify({"error": "Tweet ID must be valid"}), 400
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/retweet', methods=['POST'])
async def retweet():
    if request.is_json:
        data = request.get_json()

        if data:
            if data['tweet_id']:
                tweet = await api.tweet_details(data['tweet_id'])
                if tweet:
                    valid_login = None
                    with open('accounts.txt', 'r') as file:
                        for line in file:
                            if data['email'] in line:
                                valid_login = line.strip()
                                break
                    if valid_login:
                        username, password, email, email_password = valid_login.split(':')
                        account = Account(email, username, password)
                        account.retweet(data['tweet_id'])
                        return True
                    else:
                        return jsonify({"error": "Email must be valid"}), 400
                else:
                    return jsonify({"error": "Tweet ID must be valid"}), 400
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400

async def main():
    
    with open('accounts.txt', 'r') as file:
        for line in file:
            try:
                username, password, email, email_password = line.strip().split(':')
                await api.pool.add_account(username, password, email, email_password)
            except:
                continue
    
    await api.pool.login_all()

if __name__ == "__main__":
    asyncio.run(main())
    print("Running!")
    app.run(port=5000)
