# https://leetcode.com/problems/decode-string/description/


class Solution:
    def decodeString(self, s: str) -> str:
        s_list: list[str] = [c for c in s]
        stack = ['']
        for i, char in enumerate(s_list):
            if char.isdigit():
                if str(stack[-1]).isdigit():
                    new_int = f'{stack.pop()}{char}'
                    stack.append(int(new_int))
                else:
                    stack.append(int(char))
            elif char == '[':
                stack.append('')
            elif char.isalnum():
                if stack[-1].isalnum():
                    stack[-1] = stack[-1]+char
                else:
                    stack.append(char)
            elif char == ']':
                str_ = stack.pop()
                add_ = stack.pop()
                num = stack.pop()
                new_str = num*f'{add_}{str_}'
                if stack[-1].isalnum():
                    stack[-1] = stack[-1] + new_str
                else:
                    stack.append(new_str)
        return ''.join(stack)



print(Solution().decodeString('2[ab]3[c]'))  # ababccc
print(Solution().decodeString('3[a2[c]]'))  # accaccacc
print(Solution().decodeString('10[leetcode]'))
