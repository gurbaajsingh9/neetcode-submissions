class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        t = 'yes'
        b = {
                '(':')',
                '{':'}',
                '[':']'
            }
        for i in s:
            if i in b:
                st.append(i)
            else:
                if not st:
                    return False
                top = st.pop()
                if i == ']'  and top == '[':
                    t = 'yes'
                elif i == '}' and top == '{':
                    t = 'yes'
                elif i == ')' and top == '(':
                    t = 'yes'
                else:
                    return False
        if t == 'yes' and not st:
            return True
        else:
            return False