class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)

        self.heap = []
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.heap, (-self.timestamp, userId, tweetId))
        self.timestamp+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        temp = []

        while self.heap and len(tweets) < 10:

            recent, user, tweet = heapq.heappop(self.heap)
            temp.append((recent, user, tweet))

            if user in self.followers[userId] or user == userId:
                tweets.append(tweet)

        for i in range(len(temp)):
            heapq.heappush(self.heap, temp[i])

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in  self.followers[followerId]:
                self.followers[followerId].remove(followeeId)


        
