class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i, string in enumerate(strs):
            temp_str = string + ";;"
            encoded_string += temp_str
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return s.split(";;")[:-1]