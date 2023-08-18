from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0:
            return len(tasks)
        
        freq = Counter(tasks)
        max_freq = Counter.most_common(freq, 1)[0][1]
        freq = list(freq.values())

        last_row = freq.count(max_freq)
        #그 전줄까진 max 값과 같은 원소들로 꽉 차있을 것.
        #last_row는 max값과 같은 count의 원소만이 있을 것
        
        ans = (max_freq - 1) * (n + 1) + last_row
        return max(len(tasks),ans)