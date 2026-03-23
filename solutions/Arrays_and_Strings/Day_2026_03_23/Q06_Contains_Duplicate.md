# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. The function should return true if there are any duplicates and false otherwise. The array can contain negative numbers and zero. The function should be able to handle large arrays efficiently. For example, given the array [1, 2, 3, 1], the function should return true because the number 1 is duplicated. Given the array [1, 2, 3, 4], the function should return false because there are no duplicates.

## Approach
The approach to solve this problem is to use an unordered set to store the elements of the array as we iterate through it. If we encounter an element that is already in the set, we return true because it's a duplicate. If we finish iterating through the array without finding any duplicates, we return false.

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
            // If the current element is already in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the current element to the set
            uniqueElements.insert(num);
        }
        // If we finish iterating through the array without finding any duplicates, return false
        return false;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 1]
Output: true
Input: [1, 2, 3, 4]
Output: false
Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

## Key Takeaways
- Use an unordered set to store unique elements for efficient lookup.
- Iterate through the array and check for duplicates by looking up each element in the set.
- Return true as soon as a duplicate is found, and false if no duplicates are found after iterating through the entire array.