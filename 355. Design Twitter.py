import heapq
from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        # Global timestamp to track tweet recency
        self.timestamp = 0
        # userId -> list of [timestamp, tweetId]
        self.tweets = defaultdict(deque)
        # userId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1  # Use negative for a Min-Heap to act as a Max-Heap
        # Store only the last 10 tweets per user to save space
        self.tweets[userId].appendleft([self.timestamp, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        # A user follows themselves for the purpose of the feed
        self.following[userId].add(userId)
        
        for followee_id in self.following[userId]:
            if followee_id in self.tweets:
                index = 0
                tweet = self.tweets[followee_id][index]
                # [timestamp, tweetId, followee_id, next_index]
                min_heap.append([tweet[0], tweet[1], followee_id, index + 1])
        
        heapq.heapify(min_heap)
        
        while min_heap and len(res) < 10:
            t_stamp, t_id, f_id, next_idx = heapq.heappop(min_heap)
            res.append(t_id)
            
            # If the followee has more tweets, push the next one into the heap
            if next_idx < len(self.tweets[f_id]):
                next_tweet = self.tweets[f_id][next_idx]
                heapq.heappush(min_heap, [next_tweet[0], next_tweet[1], f_id, next_idx + 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)