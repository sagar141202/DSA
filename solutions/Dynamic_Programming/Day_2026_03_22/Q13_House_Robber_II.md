# House Robber II

## Problem Statement
The problem involves finding the maximum amount of money that can be stolen from a circular array of houses, with the constraint that no two adjacent houses can be robbed. Each house has a certain amount of money, and the goal is to maximize the total amount stolen. The houses are arranged in a circle, meaning that the first house is adjacent to the last house.

## Approach
The problem can be solved using dynamic programming by breaking it down into two cases: one where the first house is robbed and one where it is not. The maximum amount of money that can be stolen in each case is calculated separately. The algorithm uses a bottom-up approach to fill up a table with the maximum amount of money that can be stolen up to each house.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        if (n == 2) return max(nums[0], nums[1]);

        // case 1: rob the first house
        vector<int> dp1(n);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // case 2: do not rob the first house
        vector<int> dp2(n);
        dp2[0] = 0;
        dp2[1] = nums[1];
        for (int i = 2; i < n; i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }

        return max(dp1[n-2], dp2[n-1]);
    }
};
```

## Test Cases
```
Input: [2,3,2]
Output: 3
Input: [1,2,3,1]
Output: 4
Input: [0]
Output: 0
```

## Key Takeaways
- The problem requires breaking it down into two cases to handle the circular constraint.
- Dynamic programming is used to efficiently calculate the maximum amount of money that can be stolen in each case.
- The time complexity is O(n) because we are filling up two tables of size n.