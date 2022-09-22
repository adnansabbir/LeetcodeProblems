function reverseWords(s: string): string {
    const sSplitted = s.split(' ')
    for(let i = 0; i<sSplitted.length; i++){
        sSplitted[i] = sSplitted[i].split('').reverse().join('')
    }
    
    return sSplitted.join(' ')
};