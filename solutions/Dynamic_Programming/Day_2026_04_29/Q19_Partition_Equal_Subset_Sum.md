# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in `nums` can only be used once in the partition. The length of `nums` is in the range `[1, 200]`, and the sum of `nums` is in the range `[1, 10^4]`. For example, given `nums = [1, 5, 11, 5]`, the function should return `true` because `nums` can be partitioned into `[1, 5, 5]` and `[11]` with equal sum.

## Approach
This problem can be solved using dynamic programming by calculating the possible sums that can be achieved with the given numbers. We start with a sum of 0 and then iteratively add each number to the possible sums, marking the sums that can be achieved. The algorithm checks if the total sum of the array can be divided into two equal parts.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array
- Space: O(sum), for storing the dynamic programming table

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
- The problem can be solved using dynamic programming by iterating over the numbers and possible sums.
- The time complexity depends on the sum of the numbers and the number of elements in the array.
- The space complexity depends on the sum of the numbers.