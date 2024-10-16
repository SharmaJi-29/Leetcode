class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []
        if a > 0 :
            heapq.heappush(maxheap, (-a, 'a'))
        if b > 0 :
            heapq.heappush(maxheap, (-b, 'b'))
        if c > 0 :
            heapq.heappush(maxheap, (-c, 'c'))

        
        result = []

        while maxheap :
            count, char = heapq.heappop(maxheap)
            count = - count

            if (
                len(result) >= 2 and
                result[-1] == char and
                result[-2] == char
                ):

                if not maxheap:
                    break
                
                tempCnt, tempChar = heapq.heappop(maxheap)
                result.append(tempChar)

                if (tempCnt + 1) < 0:
                    heapq.heappush(maxheap, (tempCnt + 1, tempChar))
                heapq.heappush(maxheap, (-count, char))

            else :
                count -= 1
                result.append(char)

                if count > 0:
                    heapq.heappush(maxheap, (-count, char))

        return "".join(result)