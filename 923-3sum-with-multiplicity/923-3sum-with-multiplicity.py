class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        mod = 10**9 + 7
        total = 0
        
        for i, x in enumerate(arr):
            T = target - x
            j, k = i+1, len(arr) - 1
            
            while j < k:
                if arr[j] + arr[k] < T:
                    j +=1
                elif arr[j] + arr[k] > T:
                    k -=1
                elif arr[j] != arr[k]:
                    left  = right = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        right += 1
                        k -= 1
                    
                    total += left * right
                    total %= mod
                    j += 1
                    k -= 1
                else:
                    total += (k-j + 1) * (k-j) / 2
                    total %=mod
                    break

        return int(total)
                    