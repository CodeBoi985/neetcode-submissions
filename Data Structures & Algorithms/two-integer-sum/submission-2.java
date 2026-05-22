class Solution {
    public int[] twoSum(int[] nums, int target) {
        // create hashmap
        Map<Integer, Integer> numMap = new HashMap<>();

        // Loop through nums
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];

            if (numMap.containsKey(complement)){
                return new int[] {numMap.get(complement), i};
            }

            numMap.put(nums[i], i);
        }
        return new int[] {};
    }
}
