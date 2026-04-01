# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the input array is in the range [1, 200] and the sum of values in the array is in the range [1, 10^4]. The array can contain duplicate values.

## Approach
We can solve this problem using dynamic programming, where we calculate the total sum of the array and then try to find a subset that sums up to half of the total sum. The idea is to use a boolean array `dp` where `dp[i]` is `true` if there exists a subset that sums up to `i`.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array.
- Space: O(sum), where sum is the total sum of the array.

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
    cout << boolalpha << solution.canPartition(nums) << endl;
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
- The problem can be reduced to finding a subset that sums up to half of the total sum of the array.
- Dynamic programming can be used to solve this problem efficiently by avoiding redundant calculations.
- The time complexity of the solution is O(n * sum), where n is the number of elements in the array and sum is the total sum of the array.