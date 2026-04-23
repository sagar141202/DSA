# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` if all elements are unique. The function should be able to handle arrays of size up to `10^5` and integers in the range `[-10^9, 10^9]`. For example, given the array `[1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. However, given the array `[1, 2, 3, 4]`, the function should return `false` because all elements are unique.

## Approach
The approach to solve this problem is to use an unordered set to store unique elements from the array. We iterate through the array and for each element, we check if it already exists in the set. If it does, we return `true` immediately. If we finish iterating through the array without finding any duplicates, we return `false`. This approach works because sets in C++ have an average time complexity of O(1) for insertion and search operations.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // Create an unordered set to store unique elements
        unordered_set<int> uniqueElements;
        
        // Iterate through the array
        for (int num : nums) {
            // If the element already exists in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, insert the element into the set
            uniqueElements.insert(num);
        }
        // If we finish iterating without finding duplicates, return false
        return false;
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3, 1]
Output: true
Input: nums = [1, 2, 3, 4]
Output: false
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

## Key Takeaways
- Using an unordered set allows for efficient duplicate detection with an average time complexity of O(1) for insertion and search operations.
- The overall time complexity of the solution is O(n) because we iterate through the array once.
- The space complexity is also O(n) because in the worst-case scenario, we might need to store all elements in the set.