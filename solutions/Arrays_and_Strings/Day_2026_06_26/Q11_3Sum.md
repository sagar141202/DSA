# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array which gives the sum of zero. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`. The array can contain duplicate elements and the length of the array can be up to 10^4.

## Approach
The algorithm uses a two-pointer technique with sorting. First, sort the array, then for each element, use two pointers starting from the next element and the end of the array to find a pair that sums up to the negation of the current element.

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
            // Skip duplicates for i
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Use two pointers to find a pair
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) left++;
                else if (sum > 0) right--;
                else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    // Skip duplicates for left and right
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
- Sorting the array helps in applying the two-pointer technique efficiently.
- Skipping duplicates for the current element and the two pointers helps in avoiding duplicate triplets in the result.
- The two-pointer technique allows us to find a pair that sums up to the negation of the current element in linear time.