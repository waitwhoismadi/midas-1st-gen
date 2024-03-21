import praw

reddit = praw.Reddit(client_id='madi',
                     client_secret='secret',
                     user_agent='wait_whoismadi')

subreddit_name = 'python'

subreddit = reddit.subreddit(subreddit_name)

num_posts = 10

top_posts = subreddit.top(limit=num_posts)

for post in top_posts:
    print("Title:", post.title)
    print("Score:", post.score)
    print("URL:", post.url)
