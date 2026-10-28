import heapq

class AuctionSystem:

    def __init__(self):
        self.items = {}  # itemId -> {bids, heap}

    def addBid(self, userId, itemId, bidAmount):
        if itemId not in self.items:
            self.items[itemId] = {"bids": {}, "heap": []}
        
        self.items[itemId]["bids"][userId] = bidAmount
        heapq.heappush(self.items[itemId]["heap"], (-bidAmount, -userId))

    def updateBid(self, userId, itemId, newAmount):
        self.items[itemId]["bids"][userId] = newAmount
        heapq.heappush(self.items[itemId]["heap"], (-newAmount, -userId))

    def removeBid(self, userId, itemId):
        del self.items[itemId]["bids"][userId]

    def getHighestBidder(self, itemId):
        if itemId not in self.items or not self.items[itemId]["bids"]:
            return -1
        
        bids = self.items[itemId]["bids"]
        heap = self.items[itemId]["heap"]
        
        while heap:
            amount, user = heap[0]
            amount = -amount
            user = -user
            
            if user in bids and bids[user] == amount:
                return user
            heapq.heappop(heap)  # remove stale entry
        
        return -1