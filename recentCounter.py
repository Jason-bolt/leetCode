class RecentCounter:

    def __init__(self):
        self.request: int = 0
        self.request_set: List[int] = []
        self.previous_minimum: int = -3000
        
    def ping(self, t: int) -> int:
        request = 0
        if self.request_set == []:
            request += 1
            self.request_set.append(t)
            self.request = request
            return self.request
        self.request_set.sort(reverse=True)
        for req in self.request_set:
            if (t - 3000) <= req:            
                request += 1
            else:
                break
        self.request = request
        self.request_set.append(t)
        return self.request + 1
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)