# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The array can contain duplicate elements, and the solution should handle this case.

## Approach
The algorithm uses a two-pointer technique to find the triplets. First, it sorts the array, then fixes one element and uses two pointers to find the other two elements that sum up to the negation of the fixed element. The algorithm skips duplicate elements to avoid duplicate triplets.

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
        // Sort the array to apply two-pointer technique
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        
        // Fix one element and use two pointers to find the other two
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) left++;
                else if (sum > 0) right--;
                else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    // Skip duplicate elements
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++; right--;
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
Input: nums = [0,1,1]
Output: []
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

## Key Takeaways
- The two-pointer technique is useful for finding pairs or triplets in a sorted array.
- Sorting the array and skipping duplicate elements can help avoid duplicate solutions.
- The algorithm has a time complexity of O(n^2) due to the nested loops.