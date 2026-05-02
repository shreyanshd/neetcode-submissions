class Twitter:

    def __init__(self):
        self.tid = 1
        self.followers = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.MAX = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.tid, tweetId))
        self.tid += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        users = {userId}.union(self.followers[userId])
        for user in users:
            tweets = self.userTweets[user]
            for i in range(len(tweets)-1, -1, -1):
                tid, tweetId = tweets[i]
                heapq.heappush(minHeap, (tid, tweetId))
                if len(minHeap) > self.MAX:
                    heapq.heappop(minHeap)
                    if tid < minHeap[0][0]:
                        break
        feed = []
        while len(feed) <= self.MAX and minHeap:
            _, tweetId = heapq.heappop(minHeap)
            feed.append(tweetId)
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
