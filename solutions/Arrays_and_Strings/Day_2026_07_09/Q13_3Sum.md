# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The array can contain duplicate elements and the length of the array is not fixed. The array can be empty, and the elements can be positive, negative, or zero.

## Approach
The algorithm uses a two-pointer technique to solve the problem. First, sort the array, then fix one element and use two pointers to find the other two elements that sum up to the negation of the fixed element. This approach ensures that all possible triplets are considered and duplicate triplets are avoided.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Sort the array to apply the two-pointer technique
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        
        // Fix one element and use two pointers to find the other two elements
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate triplets
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                // If the sum is zero, add the triplet to the result
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    
                    // Skip duplicate triplets
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                } 
                // If the sum is less than zero, move the left pointer to increase the sum
                else if (sum < 0) {
                    left++;
                } 
                // If the sum is greater than zero, move the right pointer to decrease the sum
                else {
                    right--;
                }
            }
        }
        return result;
    }
};
```

## Test Cases
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Input: nums = []
Output: []
Input: nums = [0]
Output: []
```

## Key Takeaways
- The two-pointer technique can be used to solve problems that involve finding a pair of elements in a sorted array.
- Sorting the array can help to avoid duplicate triplets and ensure that all possible triplets are considered.
- Using a `set` or `map` can also help to avoid duplicate triplets, but it may increase the space complexity of the solution.