class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 for passenger in details if int(passenger[11:13]) > 60])
        