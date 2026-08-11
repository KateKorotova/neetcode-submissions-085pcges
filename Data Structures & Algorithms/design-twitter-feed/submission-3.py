from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1
        if len(self.tweetMap[userId]) > 10:
             self.tweetMap[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        users_pool = self.followMap[userId]
        users_pool.add(userId)
        heap = []
        heapq.heapify(heap)
        for user in users_pool:
            tweets = self.tweetMap[user]
            for tweet in tweets:
                heapq.heappush(heap, tweet)
        final_feed = []
        k = 0
        while heap and k < 10:
            final_feed.append(heapq.heappop(heap)[1])
            k += 1
        return final_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
