# Longest Increasing Subsequence

## Problem Statement
The Longest Increasing Subsequence (LIS) problem is a classic problem in computer science, where given an array of integers, we need to find the length of the longest subsequence that is strictly increasing. The subsequence can be non-contiguous, meaning that the elements do not have to be adjacent to each other in the original array. For example, given the array `[10, 22, 9, 33, 21, 50, 41, 60, 80]`, the longest increasing subsequence is `[10, 22, 33, 50, 60, 80]` with a length of 6.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the longest increasing subsequence ending at that index. The final result is the maximum value in this table. The intuition is to compare each element with all previous elements and update the table accordingly.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    vector<int> dp(nums.size(), 1);
    int max_length = 1;
    for (int i = 1; i < nums.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        max_length = max(max_length, dp[i]);
    }
    return max_length;
}

int main() {
    vector<int> nums = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    cout << lengthOfLIS(nums) << endl;  // Output: 6
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
- The dynamic programming approach allows us to avoid redundant calculations and improve efficiency.
- The time complexity of O(n^2) is acceptable for most use cases, but for very large inputs, a more efficient algorithm like binary search can be used to achieve O(n log n) time complexity.
- The space complexity of O(n) is necessary to store the dynamic programming table.