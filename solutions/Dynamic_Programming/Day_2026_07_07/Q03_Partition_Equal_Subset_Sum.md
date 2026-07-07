# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be in the range of 1 to 100, and the sum of all elements will not exceed 1000. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`, which have the same sum.

## Approach
The problem can be solved using dynamic programming, where we calculate the total sum of the array and then try to find a subset that has a sum equal to half of the total sum. We use a boolean array `dp` to store whether a sum is achievable or not.

## Complexity
- Time: O(n * sum), where n is the number of elements and sum is the total sum of the array
- Space: O(sum), where sum is the total sum of the array

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

int main() {
    vector<int> nums = {1, 5, 11, 5};
    cout << boolalpha << canPartition(nums) << endl;
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
- The problem can be solved using dynamic programming, where we calculate the total sum of the array and then try to find a subset that has a sum equal to half of the total sum.
- We use a boolean array `dp` to store whether a sum is achievable or not.
- The time complexity is O(n * sum), where n is the number of elements and sum is the total sum of the array.