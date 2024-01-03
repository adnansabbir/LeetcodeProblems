class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0  # Initialize the result which will store the total number of lasers
        prevRowDeviceCount = 0  # Store the device count of the previous non-empty row

        for row in bank:  # Iterate through each row in the bank
            devicesInCurrentRow = 0  # Count the number of devices in the current row
            for cell in row:  # Iterate through each cell in the row
                devicesInCurrentRow += 1 if cell == '1' else 0  # Increment if a device is found
            
            if devicesInCurrentRow == 0:  # Skip if no devices are found in the current row
                continue
            
            # If devices are present, calculate the number of lasers with the previous row
            result += prevRowDeviceCount * devicesInCurrentRow
            prevRowDeviceCount = devicesInCurrentRow  # Update the count for the next iteration
        
        return result  # Return the total number of lasers
