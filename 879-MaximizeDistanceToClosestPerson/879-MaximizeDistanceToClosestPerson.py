# Last updated: 04/05/2026, 00:32:46
class Solution:
    '''def maxDistToClosest(self, seats: List[int]) -> int:
        count=0
        maxcount=0
        length=len(seats)
        temp_length=length
        first_count=0
        temp_count=0
        while(seats[temp_count]==0):
            first_count=first_count+1
            temp_count=temp_count+1
        for i in range(length):
            if seats[i]==1:
                count=0
            else:
                count=count+1
            if(maxcount<count):
                maxcount=count
        result = maxcount//2 if maxcount%2==0 else maxcount//2+1
        finalCount = first_count if first_count > count else count
        ans = result if result > finalCount else finalCount
        return ans
        '''
    def maxDistToClosest(self, seats: List[int]) -> int:
        L = len(seats)
        S = [i for i in range(L) if seats[i]]
        d = [S[i+1]-S[i] for i in range(len(S)-1)] if len(S) > 1 else [0]
        return max(max(d)//2, S[0], L-1-S[-1])