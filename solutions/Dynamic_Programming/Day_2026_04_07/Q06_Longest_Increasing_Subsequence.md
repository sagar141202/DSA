# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the array `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the output is `4`. The array may contain duplicates, and the length of the array is between `1` and `1000`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the longest increasing subsequence ending at that index. The final result is the maximum value in this table. The dynamic programming state is updated by comparing each element with all previous elements. If the current element is greater than a previous element, it can be appended to the increasing subsequence ending at the previous element.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    // Initialize a table to store the length of the longest increasing subsequence ending at each index
    vector<int> dp(n, 1);
    
    // Initialize the maximum length of the longest increasing subsequence
    int max_length = 1;
    
    // Iterate over the array to fill up the table
    for (int i = 1; i < n; i++) {
        // For each element, compare it with all previous elements
        for (int j = 0; j < i; j++) {
            // If the current element is greater than a previous element, update the table
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        // Update the maximum length
        max_length = max(max_length, dp[i]);
    }
    
    // Return the maximum length of the longest increasing subsequence
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
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Input: [0, 1, 0, 3, 2, 3]
Output: 4
Input: [7, 6, 5, 4, 3, 2]
Output: 1
```

## Key Takeaways
- The dynamic programming approach can be used to solve problems that have overlapping subproblems and optimal substructure.
- The time complexity of the solution can be improved using more efficient algorithms, such as binary search.
- The space complexity can be reduced by using a more compact data structure to store the dynamic programming table.