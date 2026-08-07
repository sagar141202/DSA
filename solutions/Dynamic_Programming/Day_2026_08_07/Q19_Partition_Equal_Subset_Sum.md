# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 20. Each element in the array will be between 1 and 100, and the sum of all elements will not exceed 1000. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`, which have the same sum.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The algorithm iterates over the array and for each element, it checks if the current sum can be achieved by either including or excluding the current element.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array
- Space: O(sum), where sum is the total sum of the array

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
        
        // If the sum is odd, it's impossible to partition the array into two subsets with equal sum
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
- The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum.
- The algorithm iterates over the array and for each element, it checks if the current sum can be achieved by either including or excluding the current element.
- The time complexity of the solution is O(n * sum), where n is the number of elements in the array and sum is the total sum of the array.