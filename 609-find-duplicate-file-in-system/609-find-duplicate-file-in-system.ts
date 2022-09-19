function findDuplicate(paths: string[]): string[][] {
    const contentDirMap = {}
    paths.forEach(path=> {
        const pathSplitted = path.split(' ')
        const dir = pathSplitted[0]
        for(let i = 1; i < pathSplitted.length; i++){
            const fSplit = pathSplitted[i].split('(')
            const fileName = fSplit[0]
            const content = fSplit[1].split(')')[0]
            if(contentDirMap[content] === undefined){
                contentDirMap[content] = [`${dir}/${fileName}`]
            }else{
                contentDirMap[content].push(`${dir}/${fileName}`)
            }
        }
    })
    
    const result = []
    Object.keys(contentDirMap).forEach(content=> {
        if(contentDirMap[content].length > 1){
            result.push(contentDirMap[content])
        }
    })
    return result
};