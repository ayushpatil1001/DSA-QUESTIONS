class Solution:
    def divide(self, dividend, divisor):

        # Special case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Check sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Find the biggest multiple of divisor
            while dividend >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        return result