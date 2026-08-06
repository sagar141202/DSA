# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution should not contain duplicate triplets. For example, given the array `[-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The input array can contain duplicate elements, and the length of the array is in the range `[0, 3000]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. First, the array is sorted, then for each element, two pointers are used to find a pair of elements that sum up to the negation of the current element. The algorithm skips duplicate elements to avoid duplicate triplets.

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
        
        // Iterate over the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Use two pointers to find a pair of elements that sum up to the negation of the current element
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
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

## Key Takeaways
- The two-pointer technique is used to find a pair of elements that sum up to a target value.
- Sorting the array helps to apply the two-pointer technique efficiently.
- Skipping duplicate elements is necessary to avoid duplicate triplets in the result.