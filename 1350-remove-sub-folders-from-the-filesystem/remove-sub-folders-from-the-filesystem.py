class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        result = []
        folder.sort(key=lambda x: len(x))
        for directory in folder:
            trie_pointer = trie
            take_dir = True
            for dir_name in directory.split('/'):
                if trie_pointer.get('end'):
                    take_dir = False
                    break
                elif dir_name not in trie_pointer:
                    trie_pointer[dir_name] = {}
                trie_pointer = trie_pointer.get(dir_name)
            
            if take_dir:
                trie_pointer['end'] = True
                result.append(directory)
        
        return result

