# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be in the range [1, 100]. The array may contain duplicate elements.

## Approach
The problem can be solved using dynamic programming, where we calculate the total sum of the array and check if it's possible to get a subset with a sum equal to half of the total sum. We use a DP table to store the possible sums.

## Complexity
- Time: O(n * sum)
- Space: O(n * sum)

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
        if (sum % 2 != 0) return false;
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
Input: [1, 5, 11, 5]
Output: true
```

## Key Takeaways
- The problem requires finding a subset with a sum equal to half of the total sum of the array.
- Dynamic programming is used to store the possible sums and check if the target sum is achievable.
- The time complexity is O(n * sum) and space complexity is O(n * sum), where n is the length of the array and sum is the total sum of the array.