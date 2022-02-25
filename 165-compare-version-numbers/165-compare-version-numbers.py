class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_dots = version1.count('.')
        v2_dots = version2.count('.')
        
        if v1_dots>v2_dots:
            for i in range(v2_dots, v1_dots):
                version2 += '.0'
        else:
            for i in range(v1_dots, v2_dots):
                version1 += '.0'
        
        v1_split = [int(v) for v in version1.split('.')]
        v2_split = [int(v) for v in version2.split('.')]
        
        for i, v1 in enumerate(v1_split):
            if v1 > v2_split[i]:
                return 1
            elif v1 < v2_split[i]:
                return -1
        
        return 0