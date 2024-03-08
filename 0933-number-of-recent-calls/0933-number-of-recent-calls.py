class RecentCounter:

    def __init__(self):
        self.requests = []
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        counter = 0
        i = 1
        try:
            while self.requests[-i] >= (t - 3000) and self.requests[-i] <= t:
                counter += 1
                i += 1
        finally:
            return counter

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)