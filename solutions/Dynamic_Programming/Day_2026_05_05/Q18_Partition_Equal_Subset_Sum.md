# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array is not more than 200 and the sum of elements is not more than 10000. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`.

## Approach
We can solve this problem using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The algorithm iterates over all possible subsets of the array and checks if their sum equals half of the total sum.

## Complexity
- Time: O(2^n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 != 0) return false;
        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (dp[i - num]) dp[i] = true;
            }
        }
        return dp[target];
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 5, 11, 5};
    cout << solution.canPartition(nums) << endl; // Output: 1 (true)
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 5, 11, 5]
Output: true
Input: nums = [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The problem can be solved using dynamic programming by checking all possible subsets of the array.
- The time complexity of the algorithm is exponential due to the iteration over all subsets, but it can be optimized using dynamic programming.
- The space complexity is linear as we only need to store the dynamic programming table.