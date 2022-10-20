const numCharMap = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    '10': 'J',
    '11': 'K',
    '12': 'L',
    '13': 'M',
    '14': 'N',
    '15': 'O',
    '16': 'P',
    '17': 'Q',
    '18': 'R',
    '19': 'S',
    '20': 'T',
    '21': 'U',
    '22': 'V',
    '23': 'W',
    '24': 'X',
    '25': 'Y',
    '26': 'Z'
}

function numDecodings(s: string): number {
    if(s[0] === '0') return 0
    if(s.length === 1) return 1
    
    const dp = new Array<number>(s.length).fill(0)
    dp[0] = 1
    if(numCharMap[s[1]]) dp[1] = 1
    if(numCharMap[s[0] + s[1]]) dp[1] += 1
    if(dp[1] === 0) return 0
    
    for(let i = 2; i<s.length; i++){
        let combination = 0
        if(numCharMap[s[i]] !== undefined){
            combination = dp[i-1]
        }
        if(numCharMap[s[i-1]+s[i]] !== undefined){
            combination += dp[i-2]
        }
        
        if(combination === 0) return 0
        dp[i] = combination
    }
    
    return dp[s.length-1]
};