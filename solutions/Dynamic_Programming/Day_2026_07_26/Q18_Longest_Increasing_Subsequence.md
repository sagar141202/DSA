# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The problem constraints are: `1 <= nums.length <= 10^4` and `0 <= nums[i] <= 10^9`. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output should be `4`.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. The intuition is to iterate over the array and for each element, find the maximum length of the increasing subsequence ending at previous indices that can be extended by the current element.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    // Initialize dp array with all elements as 1
    vector<int> dp(nums.size(), 1);
    
    // Initialize maximum length
    int max_length = 1;
    
    // Iterate over the array
    for (int i = 1; i < nums.size(); i++) {
        // For each element, find the maximum length of the increasing subsequence ending at previous indices
        for (int j = 0; j < i; j++) {
            // If current element is greater than previous element, update dp[i]
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        // Update maximum length
        max_length = max(max_length, dp[i]);
    }
    
    // Return maximum length
    return max_length;
}

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << lengthOfLIS(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Input: nums = [7, 6, 5, 4, 3, 2]
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`.
- The time complexity of the solution is O(n^2) due to the nested loops.
- The space complexity of the solution is O(n) as we need to store the `dp` array of size `n`.