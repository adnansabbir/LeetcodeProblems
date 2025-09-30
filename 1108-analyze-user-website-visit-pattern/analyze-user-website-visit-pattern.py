from sortedcontainers import SortedList
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        user_visit_map = {}

        for u, t, w in zip(username, timestamp, website):
            if u not in user_visit_map:
                user_visit_map[u] = SortedList(key = lambda x: (x[1]))
            
            user_visit_map[u].add((w, t))
        
        pattern_freq = {}
        result = None

        for user in user_visit_map.keys():
            ud = user_visit_map[user]
            for comb in set(combinations([w for w, t in ud], 3)):
                if comb not in pattern_freq:
                    pattern_freq[comb] = 1
                else:
                    pattern_freq[comb] += 1
                if not result:
                    result = (pattern_freq[comb], comb)
                elif pattern_freq[comb] >= result[0]:
                    if pattern_freq[comb] > result[0]:
                        result = (pattern_freq[comb], comb)
                    elif comb < result[1]:
                        result = (pattern_freq[comb], comb)
        
        return result[1]