class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for i in range(len(self.tweets)-1, -1, -1):
            if len(feed) == 10:
                return feed
            t, u = self.tweets[i]
            if u == userId or u in self.followers[userId]:
                feed.append(t)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
