const letterMap = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

const numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

function intToRoman(num: number): string {
    const getClosestNumber = () => {
        for(let i = numbers.length - 1; i>=0; i--){
            if(numbers[i] <= num) return numbers[i]
        }
    }
    
    let ans = ''
    while(num){
        const number = getClosestNumber()
        const romanLetter = letterMap[number]
        ans+=romanLetter
        num-=number
    }
    
    return ans
};