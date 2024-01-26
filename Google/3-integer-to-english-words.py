# Keep track of all numbers below 20 and all tens numbers
# Use recursion to break down the number into smaller parts
# and add the corresponding word to the result

class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            elif num < 1000:
                return below_20[num // 100] + " Hundred " + helper(num % 100)
            elif num < 1000000:
                return helper(num // 1000) + "Thousand " + helper(num % 1000)
            elif num < 1000000000:
                return helper(num // 1000000) + "Million " + helper(num % 1000000)
            else:
                return helper(num // 1000000000) + "Billion " + helper(num % 1000000000)
        
        below_20 = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen"
        }
        tens = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }

        if num == 0:
            return "Zero"
        return helper(num).strip()