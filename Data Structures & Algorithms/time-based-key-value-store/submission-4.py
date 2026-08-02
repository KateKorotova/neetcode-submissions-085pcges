class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        lst = self.keyStore.get(key, [])
        l, r = 0, len(lst) - 1
        largets_prev = ""
        while l <= r:
            mid = (l+r)//2
            if lst[mid][1] <= timestamp:
                largets_prev = lst[mid][0]
                l = mid + 1
            elif lst[mid][1] > timestamp:
                r = mid - 1
        return largets_prev
