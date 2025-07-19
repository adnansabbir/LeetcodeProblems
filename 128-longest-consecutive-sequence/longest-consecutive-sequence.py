class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nsm = {}
        longest_size = 1 if nums else 0

        def merge(start, end):
            starting_num = start.get("start")
            ending_num = end.get("end")

            new_size = start.get('size') + end.get('size')

            # Setting start node
            nsm[starting_num]['size'] = new_size
            nsm[starting_num]['end'] = ending_num
            # Setting End Node
            nsm[ending_num]['size'] = new_size
            nsm[ending_num]['start'] = starting_num

            return new_size

        for num in nums:
            if num not in nsm:
                nsm[num] = {"size": 1, "start": num, "end": num}
            else:
                continue

            snsm = nsm.get(num - 1, None)
            ensm = nsm.get(num + 1, None)

            # if boths are there merge them
            if snsm and ensm:
                merge(snsm, nsm[num])
                longest_size = max(longest_size, merge(nsm[num], ensm))
            # if -1 is there, append to it
            elif snsm:
                longest_size = max(longest_size, merge(snsm, nsm[num]))
            elif ensm:
                longest_size = max(longest_size, merge(nsm[num], ensm))

        return longest_size
