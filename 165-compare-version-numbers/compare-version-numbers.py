class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(num) for num in version1.split('.')]
        v2 = [int(num) for num in version2.split('.')]
        
        for i in range(max(len(v1), len(v2))):
            left, right = v1[i] if i < len(v1) else 0, v2[i] if i < len(v2) else 0
            if left < right:
                return -1
            elif left > right:
                return 1
        return 0
        