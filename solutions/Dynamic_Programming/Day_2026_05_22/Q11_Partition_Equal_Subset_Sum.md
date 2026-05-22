# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array is in the range [1, 200], and the sum of all the numbers in the array is in the range [1, 10^4]. The array may contain duplicate numbers.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it is possible to get a subset with a sum equal to half of the total sum. We use a 2D array to store the possible sums that can be achieved using the first `i` elements.

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
        if (sum % 2 != 0) {
            return false;
        }
        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
        }
        return dp[target];
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 5, 11, 5};
    cout << solution.canPartition(nums) << endl;  // Output: 1 (true)
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
- The problem requires finding a subset with a sum equal to half of the total sum of the array.
- Dynamic programming is used to store the possible sums that can be achieved using the first `i` elements.
- The time complexity is O(n * sum), where n is the length of the array and sum is the total sum of the array.