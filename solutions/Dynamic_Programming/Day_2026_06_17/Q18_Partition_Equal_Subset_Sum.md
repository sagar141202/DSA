# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array is in the range [1, 200] and the sum of all elements in the array is in the range [1, 10^4]. The array may contain duplicate elements.

## Approach
We can solve this problem by using dynamic programming to find if it's possible to get a sum equal to half of the total sum of the array. We will create a dp array where dp[i] will be true if it's possible to get a sum of i.

## Complexity
- Time: O(n * sum)
- Space: O(sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the sum is odd, it's impossible to partition the array into two subsets with equal sum.
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
    cout << boolalpha << solution.canPartition(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 5, 11, 5]
Output: true
```

## Key Takeaways
- The problem can be solved by using dynamic programming to find if it's possible to get a sum equal to half of the total sum of the array.
- We need to handle the case where the sum of the array is odd, in which case it's impossible to partition the array into two subsets with equal sum.
- The time complexity of the solution is O(n * sum), where n is the length of the array and sum is the sum of all elements in the array.