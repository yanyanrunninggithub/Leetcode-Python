#933. Number of Recent Calls 
#stack+window: time O(1) space O(1):the maximal size of our sliding window is 3000, which is a constant.
class RecentCounter:
    def __init__(self):
        self.window = []

    def ping(self, t: int) -> int:
        self.window.append(t)
        while self.window[0]<t-3000:
            self.window.pop(0)
        return len(self.window)