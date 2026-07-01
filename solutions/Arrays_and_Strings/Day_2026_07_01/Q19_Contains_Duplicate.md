# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array may contain multiple duplicates, and the duplicates can be anywhere in the array. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` is duplicated. On the other hand, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicates.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over the array, checking if each element is already in the set. If an element is found in the set, the function immediately returns `true`, indicating a duplicate. If the function iterates over the entire array without finding any duplicates, it returns `false`.

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
        
        // Iterate over the array
        for (int num : nums) {
            // If the current element is already in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the current element to the set
            uniqueElements.insert(num);
        }
        // If no duplicates are found after iterating over the entire array, return false
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
- Use an unordered set to efficiently store and look up unique elements in the array.
- Iterate over the array only once to achieve a time complexity of O(n).
- The space complexity is O(n) because in the worst-case scenario, all elements in the array are unique and must be stored in the set.