# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution should not contain duplicate triplets. For example, given the array `[-1, 0, 1, 2, -1, -4]`, the output should be `[[-1, -1, 2], [-1, 0, 1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. First, it sorts the array and then fixes one element, using two pointers starting from the next element and the end of the array to find a pair that sums up to the negation of the fixed element.

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
        
        // Fix one element and use two pointers to find a pair
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
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Key Takeaways
- The two-pointer technique is useful for finding pairs in a sorted array.
- Sorting the array and skipping duplicate elements can help avoid duplicate triplets in the result.
- The time complexity of the solution is O(n^2) due to the nested loops, where n is the size of the input array.