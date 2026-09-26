class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        key_val = {
            key: value
            for key, value in knowledge
        }

        result = ""
        recording = False
        key = ""
        for char in s:
            if char == "(":
                recording = True
                continue
            if char == ")":
                recording = False
                result += key_val.get(key, "?")
                key = ""
                # process and append to result
                continue
            
            if recording:
                key += char
            else:
                result += char

        return result
        