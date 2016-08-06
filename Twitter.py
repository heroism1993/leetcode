import time
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows=dict()
        self.tweets=dict()
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if(not self.follows.has_key(userId)):
            self.follows[userId]=set([userId])
        if(not self.tweets.has_key(userId)):
            self.tweets[userId]=list()
        
        self.tweets[userId].insert(0,(time.time(),tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if(not self.follows.__contains__(userId)):
            self.follows[userId]=set([userId])
        follows=self.follows[userId]
        newsFeed=list()
        for everyone in follows:
            if not self.tweets.__contains__(everyone):
                continue
            newsFeed.extend(self.tweets[everyone][0:10])
        
        newsFeed.sort(lambda x,y:cmp(x[0],y[0]))

        return newsFeed[0:10]



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if(not self.follows.__contains__(followerId)):
            self.follows[followerId]=set()
            self.follows[followerId].add(followerId)
        
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if(not self.follows.has_key[followerId]):
            self.follows[followerId]=set([followerId])
        else:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if(__name__=="__main__"):
    obj = Twitter()
    obj.postTweet(1,5)
    obj.getNewsFeed(1)
    obj.follow(1,2)
    obj.postTweet(2,6)
    print obj.getNewsFeed(1)
    obj.unfollow(1,2)
    print obj.getNewsFeed(1)
