# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. First, sort the array, then fix one element and use two pointers to find the other two elements that sum to the negation of the fixed element. This approach ensures that all possible triplets are considered and duplicate triplets are avoided.

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
                
                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicate triplets
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
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
- The two-pointer technique can be used to find triplets in an array that sum to a target value.
- Sorting the array is necessary to apply the two-pointer technique.
- Skipping duplicate elements is crucial to avoid duplicate triplets in the result.