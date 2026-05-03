// Last updated: 04/05/2026, 00:34:04
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i=0;
        for(int j= 0 ;j<nums.length; j++){
            for(int k=j+1;k<nums.length;k++)
            {
                if(nums[j]==target - nums[k]){
                    return new int[] {j,k};
                }
            }
        }
throw new IllegalArgumentException("No two sum solution");
    }
}