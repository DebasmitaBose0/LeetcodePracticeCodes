class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to day of the year
        def date_to_day_number(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            total_days = day
            for i in range(month - 1):
                total_days += days_in_months[i]
            return total_days
        
        # Convert all four dates to day numbers
        alice_arrive = date_to_day_number(arriveAlice)
        alice_leave = date_to_day_number(leaveAlice)
        bob_arrive = date_to_day_number(arriveBob)
        bob_leave = date_to_day_number(leaveBob)
        
        # Find the intersection of the two intervals [alice_arrive, alice_leave] and [bob_arrive, bob_leave]
        start_overlap = max(alice_arrive, bob_arrive)
        end_overlap = min(alice_leave, bob_leave)
        
        # Calculate the number of overlapping days
        if start_overlap <= end_overlap:
            return end_overlap - start_overlap + 1
        
        return 0