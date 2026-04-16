class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        value = ""
        while l <= r:
            m = l + (r - l) // 2
            t, val = values[m]
            if t > timestamp:
                r = m - 1
            else:
                value = val
                l = m + 1
        return value
