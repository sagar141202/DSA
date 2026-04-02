# Longest Increasing Subsequence

## Problem Statement
The Longest Increasing Subsequence (LIS) problem is a classic problem in computer science and mathematics. Given a sequence of integers, find the length of the longest subsequence that is strictly increasing. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the sequence [10, 22, 9, 33, 21, 50, 41, 60, 80], the longest increasing subsequence is [10, 22, 33, 50, 60, 80] with a length of 6.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the longest increasing subsequence ending at that position. The final result is the maximum value in this table. The intuition is to compare each element with all previous elements and update the table accordingly.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    // Initialize a table to store the length of LIS ending at each position
    vector<int> dp(n, 1);
    
    // Initialize the maximum length of LIS
    int max_length = 1;
    
    // Iterate over the sequence
    for (int i = 1; i < n; i++) {
        // Compare the current element with all previous elements
        for (int j = 0; j < i; j++) {
            // If the current element is greater than the previous element, update the table
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        // Update the maximum length of LIS
        max_length = max(max_length, dp[i]);
    }
    
    // Return the maximum length of LIS
    return max_length;
}

int main() {
    vector<int> nums = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    cout << "Length of LIS: " << lengthOfLIS(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
Input: [1, 2, 3, 4, 5]
Output: 5
Input: [5, 4, 3, 2, 1]
Output: 1
```

## Key Takeaways
- The Longest Increasing Subsequence problem can be solved using dynamic programming with a time complexity of O(n^2) and a space complexity of O(n).
- The algorithm iterates over the sequence and compares each element with all previous elements to update the table.
- The final result is the maximum value in the table, which represents the length of the longest increasing subsequence.