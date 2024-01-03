class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        securityDeviceCount = [sum([1 for char in row if char == '1']) for row in bank]
        securityDeviceCount = [count for count in securityDeviceCount if count > 0]
        securityDeviceCount.append(0)
        
        result = 0
        for index in range(len(securityDeviceCount) - 1):
            result += securityDeviceCount[index] * securityDeviceCount[index + 1]
        return result