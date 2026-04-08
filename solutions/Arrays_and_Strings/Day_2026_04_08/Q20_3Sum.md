# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. The input array can contain duplicate elements and the length of the array can be up to 10^4. The elements in the array can range from -10^5 to 10^5. For example, given the array `[-1, 0, 1, 2, -1, -4]`, the output should be `[[-1, -1, 2], [-1, 0, 1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. It first sorts the array, then fixes one element and uses two pointers to find the other two elements that sum up to the negation of the fixed element. The intuition is to reduce the problem to a two-sum problem.

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
        
        // Fix one element and use two pointers to find the other two elements
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements
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
                    
                    // Skip duplicate elements
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
Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input: [0, 1, 1]
Output: []

Input: [0, 0, 0]
Output: [[0, 0, 0]]
```

## Key Takeaways
- Sort the array to apply the two-pointer technique.
- Fix one element and use two pointers to find the other two elements that sum up to the negation of the fixed element.
- Skip duplicate elements to avoid duplicate triplets in the result.