# Last updated: 04/05/2026, 00:32:37
"""class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengermap={}
        for trip in trips:
            for number in range(trip[1],trip[2]):
                if number in passengermap:
                    if passengermap[number]+trip[0] > capacity:
                        return False
                    else:
                        passengermap[number] = passengermap[number]+trip[0]
                else:
                    if trip[0] > capacity:
                        return False
                    passengermap[number]=trip[0]
        return True
    """

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Because from and to is between 0 and 1000. Idea is to store counts in an array of size 1001.  
        lengthOfTrip = [ 0 for _ in range(1001)]
        
        # Update passenger change for each trip
        for trip, i, j in trips:
            lengthOfTrip[i] += trip # Increment when passenger is on board
            lengthOfTrip[j] -= trip # decrement when they depart
    
        carLoad = 0
        # Count total passenger for each bus top
        # we have the count array, we perform a line sweep from 0 to 1000 and track its total
        for i in range( len(lengthOfTrip) ):
            carLoad += lengthOfTrip[i] 
            if carLoad > capacity: # Reject when the car is overloaded somewhere
                return False                
        return True # Accept only if all trip is safe