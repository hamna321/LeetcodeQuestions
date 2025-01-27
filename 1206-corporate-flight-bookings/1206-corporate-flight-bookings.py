class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        
        for booking in bookings:
            first, last, seats = booking
            diff[first - 1] += seats  
            if last < n:  
                diff[last] -= seats
        
        Total_seats = []
        current_sum = 0
        for i in range(n):
            current_sum += diff[i]
            Total_seats.append(current_sum)
        
        return Total_seats
