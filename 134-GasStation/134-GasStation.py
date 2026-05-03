# Last updated: 04/05/2026, 00:33:25
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasleft=0
        start=0
        
        if(sum(gas)<sum(cost)):
            return -1
        
        for i in range(len(gas)):

            
            gasleft += gas[i]-cost[i]
            
            if(gasleft < 0 ):
                start=i+1
                gasleft=0
        return start
    
            
            
        