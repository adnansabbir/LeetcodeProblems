class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        result = []
        folder.sort(key=lambda x: len(x))
        # print(folder)
        for directory in folder:
            trie_pointer = trie
            take_dir = True
            for dir_name in directory.split('/'):
                # print('\t before', dir_name, trie_pointer, trie_pointer.get('end'))
                if trie_pointer.get('end'):
                    take_dir = False
                    break
                elif dir_name not in trie_pointer:
                    trie_pointer[dir_name] = {}
                trie_pointer = trie_pointer.get(dir_name)
                    
                # print('\t after', dir_name, trie_pointer)
            
            if take_dir:
                trie_pointer['end'] = True
                result.append(directory)
            # print(trie, result)
        
        return result

