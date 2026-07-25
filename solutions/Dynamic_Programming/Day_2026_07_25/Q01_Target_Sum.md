# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of ways to assign + or - sign to each integer in the array such that the sum of the resulting array equals the target sum. The array can contain both positive and negative integers, and the target sum can also be positive or negative.

## Approach
The problem can be solved using dynamic programming by iterating over the array and maintaining a frequency count of the possible sums. We can use a hashmap to store the frequency of each sum and update it accordingly. The base case is when we have only one element in the array, in which case we can assign + or - sign to it.

## Complexity
- Time: O(n*sum), where n is the number of elements in the array and sum is the maximum possible sum.
- Space: O(sum), where sum is the maximum possible sum.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the target sum is greater than the sum of all elements or less than the negative sum of all elements, return 0.
        if (S > sum || S < -sum) return 0;
        
        // Initialize a hashmap to store the frequency of each sum.
        unordered_map<int, int> dp;
        dp[0] = 1;
        
        // Iterate over the array and update the frequency of each sum.
        for (int num : nums) {
            unordered_map<int, int> temp;
            for (auto& it : dp) {
                temp[it.first + num] = temp[it.first + num] + it.second;
                temp[it.first - num] = temp[it.first - num] + it.second;
            }
            dp = temp;
        }
        
        // Return the frequency of the target sum.
        return dp[S];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], S = 3
Output: 5

Input: nums = [1], S = 1
Output: 1
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Use a hashmap to store the frequency of each sum to avoid redundant calculations.
- The problem can be solved using a bottom-up approach by iterating over the array and updating the frequency of each sum.