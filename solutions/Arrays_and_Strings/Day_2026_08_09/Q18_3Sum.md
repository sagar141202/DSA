# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The input array can contain duplicate elements and can be unsorted. The length of the input array is in the range `[3, 3000]`, and the range of the elements in the input array is `[-10^5, 10^5]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. It first sorts the array and then fixes one element, using two pointers to find the other two elements that sum up to the negation of the fixed element. The algorithm skips duplicate elements to avoid duplicate triplets.

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
        // Sort the input array
        sort(nums.begin(), nums.end());
        
        vector<vector<int>> result;
        
        // Iterate over the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Use two pointers to find the other two elements
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                // If the sum is zero, add the triplet to the result
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Move the pointers and skip duplicate elements
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                }
                // If the sum is less than zero, move the left pointer
                else if (sum < 0) {
                    left++;
                }
                // If the sum is greater than zero, move the right pointer
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

Input: nums = [0,1,1]
Output: []

Input: nums = [0,0,0]
Output: [[0,0,0]]
```

## Key Takeaways
- The two-pointer technique can be used to find triplets in an array that sum up to a target value.
- Sorting the array and skipping duplicate elements can help to avoid duplicate triplets and reduce the time complexity.
- The algorithm should handle edge cases, such as an empty input array or an array with less than three elements.