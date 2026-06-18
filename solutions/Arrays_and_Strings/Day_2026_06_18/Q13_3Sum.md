# 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution should not contain duplicate triplets. The input array may contain duplicates, and the solution should handle this case. For example, given the input `[-1,0,1,2,-1,-4]`, the output should be `[[-1,-1,2],[-1,0,1]]`.

## Approach
The algorithm uses a two-pointer technique to find the triplets. It first sorts the input array, then fixes one element and uses two pointers to find the other two elements that sum up to the negation of the fixed element. This approach ensures that all possible triplets are found without duplicates.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    // Sort the input array
    sort(nums.begin(), nums.end());
    
    vector<vector<int>> result;
    
    // Fix one element and use two pointers to find the other two elements
    for (int i = 0; i < nums.size() - 2; i++) {
        // Skip duplicates for the fixed element
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
```

## Test Cases
```
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Input: []
Output: []
Input: [0]
Output: []
```

## Key Takeaways
- The two-pointer technique is useful for finding pairs or triplets in a sorted array.
- Skipping duplicates is essential to avoid duplicate triplets in the result.
- The time complexity of the solution is O(n^2) due to the nested loops, where n is the size of the input array.