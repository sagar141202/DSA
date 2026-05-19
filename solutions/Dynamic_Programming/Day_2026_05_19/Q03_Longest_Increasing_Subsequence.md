# Longest Increasing Subsequence

## Problem Statement
The Longest Increasing Subsequence (LIS) problem is a classic problem in computer science and mathematics. Given a sequence of integers, find the length of the longest subsequence that is strictly increasing. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given the sequence [10, 22, 9, 33, 21, 50, 41, 60, 80], the longest increasing subsequence is [10, 22, 33, 50, 60, 80] with a length of 6. The sequence can contain duplicate elements and can be empty. The length of the sequence is between 1 and 10^5.

## Approach
The algorithm uses dynamic programming to solve the problem, where each element in the dp array stores the length of the longest increasing subsequence ending at that index. The dp array is filled in a bottom-up manner by comparing each element with all previous elements. If the current element is greater than the previous element, the length of the longest increasing subsequence ending at the current index is updated.

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
    int maxLen = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLen = max(maxLen, dp[i]);
    }
    return maxLen;
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
- The Longest Increasing Subsequence problem can be solved using dynamic programming with a time complexity of O(n^2).
- The dp array is used to store the length of the longest increasing subsequence ending at each index.
- The solution can be optimized using binary search to achieve a time complexity of O(n log n).