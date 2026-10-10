class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        # Count how many elements have each nonzero absolute difference.
        diff_counts = {}
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            if diff:
                diff_counts[diff] = diff_counts.get(diff, 0) + 1

        # Changing either array can reduce a difference by 1.
        remaining = k1 + k2

        # Keep differences in ascending order, so the largest is at the end.
        diff_keys = sorted(diff_counts)

        while diff_keys and remaining:
            largest = diff_keys.pop()

            # The largest difference is zero, so all differences are zero.
            if largest == 0:
                return 0

            count = diff_counts[largest]

            # Each operation lowers one occurrence of largest by 1.
            # Reduce the whole group if possible, otherwise just part of it.
            to_reduce = min(count, remaining)
            remaining -= to_reduce

            if to_reduce == count:
                del diff_counts[largest]
            else:
                diff_counts[largest] -= to_reduce

            # Move the reduced occurrences into the next lower bucket.
            lower = largest - 1
            diff_counts[lower] = diff_counts.get(lower, 0) + to_reduce

            # If lower already exists, it is now the last key.
            # Otherwise, append it to keep the keys sorted.
            if not diff_keys or diff_keys[-1] != lower:
                diff_keys.append(lower)

            # If some occurrences stayed at largest, restore that key.
            if to_reduce < count:
                diff_keys.append(largest)

        # Each bucket contributes: count × difference².
        return sum(count * diff**2 for diff, count in diff_counts.items())