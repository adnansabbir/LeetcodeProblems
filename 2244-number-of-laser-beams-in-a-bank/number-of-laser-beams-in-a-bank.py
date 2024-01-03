class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prevRowDeviceCount = 0

        for row in bank:
            devicesInCurrentRow = 0
            for cell in row:
                devicesInCurrentRow += 1 if cell == '1' else 0
            
            if devicesInCurrentRow == 0:
                continue
            
            result += prevRowDeviceCount * devicesInCurrentRow
            prevRowDeviceCount = devicesInCurrentRow
        
        return result
