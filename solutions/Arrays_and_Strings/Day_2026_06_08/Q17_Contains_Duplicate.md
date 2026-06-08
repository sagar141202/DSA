# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. A duplicate is an element that appears more than once in the array. The function should return true if any duplicates are found and false otherwise. The array can contain any type of integer (positive, negative, or zero) and can be of any size. For example, given the array [1, 2, 3, 4, 5], the function should return false because there are no duplicates. However, given the array [1, 2, 3, 2, 5], the function should return true because the number 2 is duplicated.

## Approach
The approach to solve this problem is to use an unordered set to store the elements of the array as we iterate through it. If we encounter an element that is already in the set, we return true because we have found a duplicate. If we finish iterating through the array without finding any duplicates, we return false.

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
            // If the current number is already in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the current number to the set
            uniqueElements.insert(num);
        }
        // If we finish iterating through the array without finding any duplicates, return false
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
- Using an unordered set to store unique elements allows for efficient lookup and insertion of elements.
- The time complexity of this solution is O(n) because in the worst case, we have to iterate through the entire array.
- The space complexity of this solution is O(n) because in the worst case, we have to store every element in the set.