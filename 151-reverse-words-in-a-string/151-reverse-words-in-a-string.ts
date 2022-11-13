function reverseWords(s: string): string {
    return s.split(' ').filter(s => !!s).reverse().join(' ')
};