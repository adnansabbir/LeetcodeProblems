class Solution:
    def minSteps(self, n: int) -> int:
        def get_min_count(on_notobook: int, on_clipboard: int, copied = False)-> int:
            # print(on_notobook, on_clipboard, copied)
            if on_notobook == n:
                return 0
            elif on_notobook > n or on_clipboard > n:
                return 9999
            
            if not on_clipboard:
                # print('Copy')
                return  get_min_count(on_notobook, on_notobook, True) + 1
            elif copied:
                # print('Pasting')
                return  get_min_count(on_notobook + on_clipboard, on_clipboard, False) + 1
            else:
                # print('Copy and Paste')
                return min(
                    get_min_count(on_notobook, on_notobook, True),
                    get_min_count(on_notobook + on_clipboard, on_clipboard, False)
                ) + 1
        return get_min_count(1, 0, False)
        