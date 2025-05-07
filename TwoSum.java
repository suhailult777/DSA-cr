import java.util.HashMap;

class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i }; // Return indices
            }
            map.put(nums[i], i); // Store the number and its index
        }
        throw new IllegalArgumentException("No two sum solution"); // If no solution exists
    }

    public static void main(String[] args) {
        Solution1 solution = new Solution1();

        // Use case 1: Basic test
        int[] nums1 = { 2, 7, 11, 15 };
        int target1 = 9;
        int[] result1 = solution.twoSum(nums1, target1);
        System.out.println("Use case 1: Indices are " + result1[0] + " and " + result1[1]); // Expected output: 0 and 1

        // Use case 2: Numbers at the beginning
        int[] nums2 = { 5, 5, 11, 15 };
        int target2 = 10;
        int[] result2 = solution.twoSum(nums2, target2);
        System.out.println("Use case 2: Indices are " + result2[0] + " and " + result2[1]); // Expected output: 0 and 1

        // Use case 3: No solution
        int[] nums3 = { 2, 7, 11, 15 };
        int target3 = 5;
        try {
            solution.twoSum(nums3, target3);
        } catch (IllegalArgumentException e) {
            System.out.println("Use case 3: " + e.getMessage()); // Expected output: No two sum solution
        }

        // Use case 4: Negative numbers
        int[] nums4 = { -1, -3, 7, 9 };
        int target4 = -2;
        int[] result4 = solution.twoSum(nums4, target4);
        System.out.println("Use case 4: Indices are " + result4[0] + " and " + result4[1]); // Expected output: 0 and 1

        // Use case 5: Large numbers
        int[] nums5 = { 1000, 2000, 3000, 4000 };
        int target5 = 7000;
        int[] result5 = solution.twoSum(nums5, target5);
        System.out.println("Use case 5: Indices are " + result5[0] + " and " + result5[1]); // Expected output: 2 and 3
    }
}
