import praw
import random
import os
from requests import Session
from dotenv import load_dotenv

class RandomPost:
    subreddits: dict 
    def __init__(self) -> None:
        session = Session()
        load_dotenv()
        CLIENT_ID = os.getenv('CLIENT_ID')
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        reddit = praw.Reddit(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            requestor_kwargs={"session": session},  # pass Session
                            redirect_uri="http://www.example.com/unused/redirect/uri",
                            user_agent="Grab and Dash by u/6e-6f-74-61-62-6f-74",
                            username="6e-6f-74-61-62-6f-74",
                            check_for_async=False)

        self.subreddits = {
            "memes": reddit.subreddit("memes"),
            "makemesuffer": reddit.subreddit("MakeMeSuffer"),
            "cringe": reddit.subreddit("Cringetopia"),
            "tiktok": reddit.subreddit("TikTokCringe"),
            "mademesmile": reddit.subreddit("MadeMeSmile"),
            "wholesome": [reddit.subreddit("MadeMeSmile"), reddit.subreddit("wholesomememes")],
            "anime": [reddit.subreddit("anime_irl"), reddit.subreddit("Animemes")],
            "pain":[reddit.subreddit("MakeMeSuffer"), 
                    reddit.subreddit("Cringetopia"), 
                    reddit.subreddit("TikTokCringe")]
        }

    def get_post(self, subreddit_name: str) -> None:
        if subreddit_name == "get":
            subreddit = random.choice(list(self.subreddits.values()))
        else:
            subreddit = self.subreddits[subreddit_name]
            if type(subreddit) == list:
                subreddit = random.choice(subreddit)

        post_number = random.randint(0, 50)
        i = 0
        for post in subreddit.top("week"):
            if i == post_number:
                return post.url
            i += 1



