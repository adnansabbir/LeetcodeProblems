function isMatch(s: string, p: string): boolean {
    // s = 'acdd'
    // p = 'a.*d'
    
    if(!p) return !s
    
    const firstElemMatched = s.length && [s[0], '.'].includes(p[0])
    
    if(p.length > 1 && p[1] === '*'){
        return isMatch(s, p.substring(2)) || firstElemMatched && isMatch(s.substring(1), p)
    }else{
        return firstElemMatched && isMatch(s.substring(1), p.substring(1))
    }
    
    
};