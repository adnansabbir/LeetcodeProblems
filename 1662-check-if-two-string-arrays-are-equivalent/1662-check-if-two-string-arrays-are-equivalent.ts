function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    return word1.reduce((a, c) => a+c, '') === word2.reduce((a, c) => a+c, '')
};