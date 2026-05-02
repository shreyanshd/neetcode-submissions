class Twitter:

    def __init__(self):
        self.tid = 1
        self.tweets = []
        self.followers = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.MAX = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.tid, tweetId))
        self.tid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        users = {userId}.union(self.followers[userId])
        for u in users:
            tweets = self.userTweets[u]
            for i in range(len(tweets)-1, -1, -1):
                tid, tweetId = tweets[i]
                heapq.heappush(maxHeap, (tid, tweetId))
                if len(maxHeap) > self.MAX:
                    heapq.heappop(maxHeap)
        feed = []
        while len(feed) <= self.MAX and maxHeap:
            _, tweetId = heapq.heappop(maxHeap)
            feed.append(tweetId)
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
