class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.feedLength = 10
        self.i = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.i, tweetId])
        self.i += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        users = set([userId]).union(self.follows[userId])
        for u in users:
            user_tweets = self.tweets[u]
            for i in range(len(user_tweets) - 1, -1, -1):
                heapq.heappush(minheap, user_tweets[i])
                if len(minheap) > self.feedLength:
                    heapq.heappop(minheap)
        feed = []
        while minheap:
            i, tweetId = heapq.heappop(minheap)
            feed.append(tweetId)
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
