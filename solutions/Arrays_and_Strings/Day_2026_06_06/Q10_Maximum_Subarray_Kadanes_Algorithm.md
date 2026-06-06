# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array, find the maximum sum of a contiguous subarray within the array. The array can contain both positive and negative integers. The maximum sum of a subarray is the largest possible sum of a subarray, which can be either the entire array or a part of it. For example, given the array `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the maximum sum of a subarray is `6`, which is the sum of the subarray `[4, -1, 2, 1]`.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray by iterating through the array and at each step, deciding whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum found so far. This approach ensures that all possible subarrays are considered, and the maximum sum is found efficiently.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int>& nums) {
    // Initialize the maximum sum and the current sum to the first element of the array
    int max_sum = nums[0];
    int current_sum = nums[0];
    
    // Iterate through the array starting from the second element
    for (int i = 1; i < nums.size(); i++) {
        // Update the current sum to be the maximum of the current element and the sum of the current element and the previous current sum
        current_sum = max(nums[i], current_sum + nums[i]);
        
        // Update the maximum sum to be the maximum of the current maximum sum and the current sum
        max_sum = max(max_sum, current_sum);
    }
    
    // Return the maximum sum found
    return max_sum;
}

int main() {
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Maximum sum of a subarray: " << maxSubArray(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Input: [1]
Output: 1
Input: [5, 4, -1, 7, 8]
Output: 23
```

## Key Takeaways
- Kadane's algorithm is an efficient solution for finding the maximum sum of a subarray.
- The algorithm iterates through the array only once, resulting in a time complexity of O(n).
- The space complexity is O(1) since only a constant amount of space is used to store the maximum sum and the current sum.