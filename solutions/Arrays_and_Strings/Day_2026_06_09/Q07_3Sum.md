# 3Sum

## Problem Statement
Given an array of integers, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given the array `[-1, 0, 1, 2, -1, -4]`, the output should be `[[-1, -1, 2], [-1, 0, 1]]`. The array can contain duplicate elements, and the solution should handle this case. The input array will have at least three elements.

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
        // Sort the array
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        
        // Fix one element and use two pointers to find the other two
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements
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
                    
                    // Skip duplicate elements
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
Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Key Takeaways
- The two-pointer technique can be used to find the triplets in the array.
- Sorting the array and skipping duplicate elements can help avoid duplicate triplets in the solution.
- The time complexity of the solution is O(n^2) due to the nested loops, and the space complexity is O(n) for storing the result.