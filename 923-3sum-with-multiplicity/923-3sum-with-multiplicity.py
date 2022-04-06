class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq = [0]*101
        
        for num in arr:
            freq[num]+=1
        
        mod = 10**9 + 7
        
        total = 0
        
        for x in range(101):
            for y in range(x+1, 101):
                z = target - x - y
                if y < z <=100:
                    total += freq[x] * freq[y] * freq[z]
                    total %= mod
                    
        for x in range(101):
            z = target - 2*x
            if x < z <=100:
                total += freq[x] * (freq[x] - 1)/2 * freq[z]
                total %= mod
                
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x)//2
                if x < y <=100:
                    total += freq[x] * freq[y] * (freq[y] - 1) / 2
                    total %= mod
                
        if target % 3 == 0:
            x = target//3
            if 0 <= x <=100:
                total += freq[x] * (freq[x] - 1) * (freq[x] - 2) / 6
                total %= mod
        
        return int(total)