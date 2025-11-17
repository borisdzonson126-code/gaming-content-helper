#!/usr/bin/env python3
"""
Reddit Gaming Content Helper Bot
Example implementation for API access request
"""

import os
import praw
from dotenv import load_dotenv

class RedditGamingBot:
    def __init__(self):
        load_dotenv()
        
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent="gaming_content_helper_bot v1.0 (by u/YourUsername)"
        )
    
    def get_gaming_news(self, subreddit_name='gaming', limit=10):
        """Fetch recent posts from gaming subreddits"""
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            posts = []
            
            for post in subreddit.new(limit=limit):
                posts.append({
                    'title': post.title,
                    'score': post.score,
                    'url': post.url,
                    'created': post.created_utc
                })
            
            return posts
            
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []
    
    def analyze_content_trends(self):
        """Analyze trending topics in gaming communities"""
        # This is where your content aggregation logic would go
        gaming_posts = self.get_gaming_news('gaming')
        game_deals = self.get_gaming_news('GameDeals')
        
        return {
            'gaming_news_count': len(gaming_posts),
            'deals_count': len(game_deals),
            'sample_titles': [post['title'] for post in gaming_posts[:3]]
        }

if __name__ == "__main__":
    # Example usage
    bot = RedditGamingBot()
    trends = bot.analyze_content_trends()
    print(f"Found {trends['gaming_news_count']} gaming posts")
    print(f"Sample titles: {trends['sample_titles']}")
