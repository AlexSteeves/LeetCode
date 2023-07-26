import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> itemMap = new HashMap<>();

        for (int i=0; i< nums.length; i++){
            int missingNumber = target - nums[i];

            if(itemMap.containsKey(missingNumber)){
                return new int[]{i, itemMap.get(missingNumber)};
            }else{
                itemMap.put(nums[i], i);
            }
        }
        return new int[0];
    }
}
