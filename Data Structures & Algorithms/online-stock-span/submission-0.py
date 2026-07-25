class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        c = 0
        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices[i] > price:
                return c
            c += 1
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)