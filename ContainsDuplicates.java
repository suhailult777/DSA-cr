import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (!set.add(num)) {
                return true; // Duplicate found
            }
        }
        return false; // No duplicates found
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1: Array with duplicates
        int[] nums1 = { 1, 2, 3, 4, 5, 1 };
        System.out.println(solution.containsDuplicate(nums1)); // Output: true

        // Test case 2: Array without duplicates
        int[] nums2 = { 1, 2, 3, 4, 5 };
        System.out.println(solution.containsDuplicate(nums2)); // Output: false

        // Test case 3: Empty array
        int[] nums3 = {};
        System.out.println(solution.containsDuplicate(nums3)); // Output: false

        // Test case 4: Array with one element
        int[] nums4 = { 42 };
        System.out.println(solution.containsDuplicate(nums4)); // Output: false

        // Test case 5: Array with all elements the same
        int[] nums5 = { 7, 7, 7, 7 };
        System.out.println(solution.containsDuplicate(nums5)); // Output: true
    }
}