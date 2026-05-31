# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be in the range [1, 100]. The array will not contain duplicate elements.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to achieve a sum equal to half of the total sum. The algorithm iterates over the array and for each element, it checks if including the current element can lead to the desired sum.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array.
- Space: O(sum), for storing the dynamic programming table.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 2 != 0) {
            return false;
        }
        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (dp[i - num]) {
                    dp[i] = true;
                }
            }
        }
        return dp[target];
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 5, 11, 5};
    cout << solution.canPartition(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [1, 5, 11, 5]
Output: true
Input: [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The dynamic programming approach is used to store the intermediate results and avoid redundant calculations.
- The problem can be reduced to the subset sum problem, which is a classic problem in computer science and mathematics.
- The time complexity is exponential in the size of the input array, but it's acceptable for the given constraints.