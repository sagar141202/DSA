# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution should not contain duplicate triplets. For example, given `nums = [-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. First, the array is sorted, then for each element, two pointers are used to find a pair that sums up to the negation of the current element. The algorithm skips duplicate triplets to ensure uniqueness.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    // Sort the array
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    
    // Iterate over the array
    for (int i = 0; i < nums.size() - 2; i++) {
        // Skip duplicate triplets
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        // Initialize two pointers
        int left = i + 1;
        int right = nums.size() - 1;
        
        // Find a pair that sums up to the negation of the current element
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
```

## Test Cases
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

## Key Takeaways
- Sort the array to apply the two-pointer technique.
- Skip duplicate triplets to ensure uniqueness.
- Use two pointers to find a pair that sums up to the negation of the current element.