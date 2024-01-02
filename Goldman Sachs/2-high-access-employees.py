from typing import List

# Convert the time to int (mins since midnight) and put in a hash mapping emp -> [login times in array]
# Sort the array for each emp, and check for emp logging in thrice in an hour

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def mins_since_day(time):
            hour = int(time[:2])
            return (hour * 60) + int(time[2:])

        hash = {}
        for emp, time in access_times:
            if emp in hash:
                hash[emp].append(mins_since_day(time))
            else:
                hash[emp] = [mins_since_day(time)]
        
        res = []
        for emp in hash.keys():
            if len(hash[emp]) < 3:
                continue
            hash[emp].sort()
            for i in range(2, len(hash[emp])):
                if hash[emp][i] - hash[emp][i-1] < 60 and hash[emp][i] - hash[emp][i-2] < 60:
                    res.append(emp)
                    break
        
        return res
            