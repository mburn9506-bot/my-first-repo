import java.util.HashMap;

public class TwoSumExample {

    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // check if complement exists in map
            if (map.containsKey(complement)) {
                // return the pair of indices
                return new int[] { map.get(complement), i };
            }

            // store the current number and its index
            map.put(nums[i], i);
        }

        // return empty if not found
        return new int[] {};
    }

    public static void main(String[] args) {
        int[] nums = {3, 6, 11, 15};
        int target = 9;

        int[] result = twoSum(nums, target);

        if (result.length == 2) {
            System.out.println("Indices found: " + result[0] + " and " + result[1]);
            System.out.println("Values: " + nums[result[0]] + " + " + nums[result[1]] + " = " + target);
        } else {
            System.out.println("No two numbers add up to the target.");
        }
    }
}

