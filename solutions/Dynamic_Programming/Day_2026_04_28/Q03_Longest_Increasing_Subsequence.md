# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS) in the array. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the LIS is `[2, 3, 7, 101]` and its length is `4`. The array can contain duplicate elements and can be unsorted.

## Approach
The algorithm uses dynamic programming to build up a solution by computing the length of the LIS ending at each position in the array. It iterates over the array and for each element, it checks all previous elements to find the maximum length of the increasing subsequence ending at the current position. The maximum length found is stored in a dynamic programming table.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    // Base case: If the array is empty, return 0
    if (nums.empty()) {
        return 0;
    }

    // Initialize a dynamic programming table with size equal to the array length
    vector<int> dp(nums.size(), 1);

    // Initialize the maximum length of the LIS
    int maxLength = 1;

    // Iterate over the array
    for (int i = 1; i < nums.size(); i++) {
        // For each element, check all previous elements
        for (int j = 0; j < i; j++) {
            // If the current element is greater than the previous element, update the dp table
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        // Update the maximum length of the LIS
        maxLength = max(maxLength, dp[i]);
    }

    // Return the maximum length of the LIS
    return maxLength;
}

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << "Length of LIS: " << lengthOfLIS(nums) << endl;
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
- The dynamic programming approach is suitable for solving problems that have overlapping subproblems and optimal substructure.
- The time complexity of the solution is O(n^2) due to the nested loops, where n is the length of the input array.
- The space complexity of the solution is O(n) due to the dynamic programming table.