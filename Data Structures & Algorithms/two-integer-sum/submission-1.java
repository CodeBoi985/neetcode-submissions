class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length; j++){
                if (j == i)
                    j++;
                else
                {
                    int sum = nums[i] + nums[j];
                    if (sum == target){
                        int[] answer = new int[2];
                        answer[0] = i;
                        answer[1] = j;
                        java.util.Arrays.sort(answer);
                        return answer;
                    }
                }

            }
        }
        return null;
    }
}
