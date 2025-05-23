class Solution:
    def whichWeekDay(self, day):
        switcher = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        return switcher.get(day, "Invalid day")
    
if __name__ == "__main__":
    s = Solution()
    print(s.whichWeekDay(3))
    print(s.whichWeekDay(8))