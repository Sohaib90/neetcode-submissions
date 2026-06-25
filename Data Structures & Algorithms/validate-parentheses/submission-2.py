class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        for brac in s:
            if brac in ["[", "{", "("]:
                stack.append(brac)
            else:
                if len(stack):
                    brac_pop = stack.pop()
                else:
                    brac_pop = ""
                if brac == "]" and not brac_pop == "[":
                    return False
                if brac == ")" and not brac_pop == "(":
                    return False
                if brac == "}" and not brac_pop == "{":
                    return False

        if len(stack): return False
        return True