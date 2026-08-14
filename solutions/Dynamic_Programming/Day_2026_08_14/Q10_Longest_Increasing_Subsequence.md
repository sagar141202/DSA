# Longest Increasing Subsequence

## Problem Statement
The Longest Increasing Subsequence (LIS) problem is a classic problem in computer science and mathematics. Given a sequence of integers, find the length of the longest subsequence that is strictly increasing. The subsequence can be non-contiguous, meaning that the elements do not have to be adjacent to each other in the original sequence. For example, given the sequence [10, 22, 9, 33, 21, 50, 41, 60, 80], the longest increasing subsequence is [10, 22, 33, 50, 60, 80] with a length of 6. The sequence can contain duplicate elements and can be of any length.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining an array where each element represents the length of the longest increasing subsequence ending at that index. The value of each element is calculated by comparing it with all previous elements and updating the maximum length found so far. This approach ensures that the solution is efficient and scalable for large inputs.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
    if (nums.empty()) return 0;
    
    vector<int> dp(nums.size(), 1);
    int maxLength = 1;
    
    for (int i = 1; i < nums.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLength = max(maxLength, dp[i]);
    }
    
    return maxLength;
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems and optimal substructure.
- The time complexity can be improved to O(n log n) using a binary search approach.
- The problem can be modified to find the actual longest increasing subsequence, not just its length, by maintaining additional data structures to store the subsequence.