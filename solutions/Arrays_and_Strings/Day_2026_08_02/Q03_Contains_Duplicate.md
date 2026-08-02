# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. A duplicate is an element that appears more than once in the array. The function should return true if any duplicates are found and false otherwise. The array can contain any type of integer (positive, negative, or zero) and can be of any size. For example, given the array [1, 2, 3, 4, 5], the function should return false, while given the array [1, 2, 3, 2, 5], the function should return true.

## Approach
We can solve this problem by using an unordered set to store the elements we have seen so far. We iterate over the array and for each element, we check if it is already in the set. If it is, we return true, indicating that a duplicate has been found. If we finish iterating over the array without finding any duplicates, we return false.

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
        // Create an unordered set to store the elements we have seen
        unordered_set<int> seen;
        
        // Iterate over the array
        for (int num : nums) {
            // If the element is already in the set, return true
            if (seen.find(num) != seen.end()) {
                return true;
            }
            // Otherwise, add the element to the set
            seen.insert(num);
        }
        
        // If we finish iterating over the array without finding any duplicates, return false
        return false;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: false
Input: [1, 2, 3, 2, 5]
Output: true
Input: [1, 1, 1, 1, 1]
Output: true
```

## Key Takeaways
- Using an unordered set allows us to check for duplicates in O(1) time on average.
- This solution works for arrays of any size and can contain any type of integer.
- The space complexity is O(n) because in the worst-case scenario, we might have to store all elements in the set.