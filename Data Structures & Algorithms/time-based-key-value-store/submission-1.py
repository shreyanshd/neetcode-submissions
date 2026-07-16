class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        lo = 0
        hi = len(values) - 1
        value = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            t, val = values[mid]
            if t > timestamp:
                hi = mid - 1
            else:
                value = val
                lo = mid + 1
        return value
