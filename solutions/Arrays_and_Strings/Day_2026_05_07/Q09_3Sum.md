# 3Sum

## Problem Statement
Given an array of integers `nums`, find all triplets in the array which have a sum of zero. The solution should not contain duplicate triplets. The array can contain duplicate elements, and the triplets should be returned in any order. For example, given the array `[-1, 0, 1, 2, -1, -4]`, the output should be `[[-1, -1, 2], [-1, 0, 1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. It first sorts the array, then iterates over each element, using two pointers to find a pair of elements that sum up to the negation of the current element. The intuition is to balance the sum of the three elements to zero.

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
        
        // Iterate over each element in the array
        for (int i = 0; i < nums.size() - 2; i++) {
            // Skip duplicate elements to avoid duplicate triplets
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Initialize two pointers
            int left = i + 1;
            int right = nums.size() - 1;
            
            // Find a pair of elements that sum up to the negation of the current element
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) left++;
                else if (sum > 0) right--;
                else {
                    result.push_back({nums[i], nums[left], nums[right]});
                    // Skip duplicate elements to avoid duplicate triplets
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
```

## Key Takeaways
- The two-pointer technique can be applied to find a pair of elements that sum up to a target value in a sorted array.
- Sorting the array and skipping duplicate elements can help avoid duplicate triplets in the result.
- The time complexity of the algorithm is O(n^2) due to the nested loops, where n is the size of the input array.