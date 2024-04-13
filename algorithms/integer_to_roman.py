# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:

        roman_int_map = {
            10: ['I', 'X', 'C', 'M'],
            5: ['V', 'L', 'D'],
        }

        num_str = str(num)
        res = ''
        for ten_pow, number in enumerate(reversed(num_str)):
            ten = roman_int_map[10][ten_pow]
            next_ten = roman_int_map[10][ten_pow+1] if ten_pow < 3 else ''
            five = roman_int_map[5][ten_pow] if ten_pow < 3 else ''
            number = int(number)
            match number:
                case 1 | 2 | 3:
                    roman_digit = number * ten
                case 4:
                    roman_digit = f'{ten}{five}'
                case 5:
                    roman_digit = five
                case 6 | 7 | 8:
                    roman_digit = f'{five}{(number - 5) * ten}'
                case 9:
                    roman_digit = f'{ten}{next_ten}'
                case _:
                    roman_digit = ''

            res = roman_digit + res

        return res


print(Solution().intToRoman(1994))  # MCMXCIV
