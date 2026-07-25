class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        l = 0
        r = len(people)-1
        
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1

        if l == r:
            boats += 1

        return boats 