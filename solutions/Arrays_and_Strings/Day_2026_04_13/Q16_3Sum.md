# 3Sum

## Problem Statement
Given an integer array `nums`, find all unique triplets in the array that sum to zero. The solution should not contain duplicate triplets. The input array can contain duplicate elements, and the solution should handle this case. The array can have a length of up to 10^4 elements, and each element can be in the range of -10^5 to 10^5.

## Approach
The algorithm uses the two-pointer technique to find the triplets. It first sorts the array and then fixes one element, using two pointers to find the other two elements that sum to the negation of the fixed element. The algorithm skips duplicate elements to avoid duplicate triplets.

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
        // Skip duplicate elements
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        int left = i + 1;
        int right = nums.size() - 1;
        
        // Use two pointers to find the other two elements
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
```

## Test Cases
```
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Key Takeaways
- The two-pointer technique can be used to find triplets in an array that sum to a target value.
- Sorting the array and skipping duplicate elements can help avoid duplicate triplets in the solution.
- The algorithm has a time complexity of O(n^2) due to the nested loops, where n is the length of the input array.