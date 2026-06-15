# Longest Increasing Subsequence

## Problem Statement
The Longest Increasing Subsequence (LIS) problem is a classic problem in computer science and mathematics. Given a sequence of integers, find the length of the longest subsequence that is strictly increasing. The subsequence can be non-contiguous, meaning that the elements do not have to be adjacent in the original sequence. For example, given the sequence [10, 22, 9, 33, 21, 50, 41, 60, 80], the longest increasing subsequence is [10, 22, 33, 50, 60, 80] with a length of 6. The sequence can contain duplicate elements and can be empty.

## Approach
The algorithm uses dynamic programming to build up a table of lengths of the longest increasing subsequences ending at each position. The intuition is to compare each element with all previous elements and update the length of the longest increasing subsequence if a longer one is found. The final answer is the maximum length found in the table.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    if (nums.empty()) return 0;
    int n = nums.size();
    vector<int> dp(n, 1);
    int max_length = 1;
    for (int i = 1; i < n; i++) {
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
    cout << lengthOfLIS(nums) << endl;
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
- The dynamic programming approach is used to solve the problem efficiently.
- The time complexity is O(n^2) due to the nested loops, where n is the length of the input sequence.
- The space complexity is O(n) for storing the lengths of the longest increasing subsequences ending at each position.