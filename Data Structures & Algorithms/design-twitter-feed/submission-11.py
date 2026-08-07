class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.feedLength = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        users = {userId}.union(self.follows[userId])
        for user in users:
            tweets = self.tweets[user]
            for i in range(len(tweets) - 1, -1, -1):
                t, tweetId = tweets[i]
                heapq.heappush(minheap, (t, tweetId))
                if len(minheap) > self.feedLength:
                    heapq.heappop(minheap)
                    if t < minheap[0][0]:
                        break
        feed = []
        while minheap:
            t, tweetId = heapq.heappop(minheap)
            feed.append(tweetId)
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
