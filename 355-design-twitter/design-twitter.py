class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        # Ensure user follows themselves to see their own tweets
        self.following[userId].add(userId)
        
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                # Iterate through all tweets of the followee
                for tweet in self.tweets[followeeId]:
                    heapq.heappush(min_heap, tweet)
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)
                        
        # Extract tweets from heap from oldest to newest within the top 10
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
            
        # Reverse to get most recent first
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # A user cannot unfollow themselves
        if followerId != followeeId and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)

  
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)