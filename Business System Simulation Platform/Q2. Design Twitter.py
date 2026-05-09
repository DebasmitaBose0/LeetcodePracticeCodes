import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)  # userId -> list of (time, tweetId)
        self.following = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # We store time as negative to use Python's min-heap as a max-heap
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        
        # A user follows themselves for the sake of the news feed
        self.following[userId].add(userId)
        
        for user in self.following[userId]:
            if user in self.tweets:
                # Get the last index of the user's tweet list
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                # Push (time, tweetId, userId, index_of_next_tweet_to_check)
                heapq.heappush(heap, (time, tweetId, user, index - 1))
        
        # Pull the 10 most recent tweets using the heap
        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                next_time, next_tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (next_time, next_tweetId, user, idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)