# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution should not contain duplicate triplets.

## Approach
The algorithm uses a two-pointer technique, sorting the array and fixing one element at a time. It then uses two pointers, one starting from the next element and one from the end, to find a pair that sums up to the negation of the fixed element.

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
        // Sort the array
        sort(nums.begin(), nums.end());
        
        vector<vector<int>> result;
        
        // Fix one element at a time
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicates for the fixed element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Use two pointers to find a pair that sums up to the negation of the fixed element
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicates for the left and right elements
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
```

## Key Takeaways
- Sort the array to apply the two-pointer technique.
- Fix one element at a time and use two pointers to find a pair that sums up to the negation of the fixed element.
- Skip duplicates for the fixed element and the left and right elements to avoid duplicate triplets in the result.