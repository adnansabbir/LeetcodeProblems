function numberOfBeams(bank: string[]): number {
    let result = 0;  // Initialize the result to store the total number of lasers
    let prevRowDeviceCount = 0;  // Store the device count of the previous non-empty row

    for (let row of bank) {  // Iterate through each row in the bank
        let devicesInCurrentRow = 0;  // Count the number of devices in the current row
        for (let cell of row) {  // Iterate through each cell in the row
            devicesInCurrentRow += cell === '1' ? 1 : 0;  // Increment if a device is found
        }

        if (devicesInCurrentRow === 0) {  // Skip if no devices are found in the current row
            continue;
        }

        // If devices are present, calculate the number of lasers with the previous row
        result += prevRowDeviceCount * devicesInCurrentRow;
        prevRowDeviceCount = devicesInCurrentRow;  // Update the count for the next iteration
    }

    return result;  // Return the total number of lasers
}
