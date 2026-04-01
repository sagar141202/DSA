# Contains Duplicate

## Problem Statement
Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct. The array can contain up to 10^5 elements, and each element can be in the range of [0, 10^5]. For example, given the array [1, 2, 3, 1], the function should return true because the number 1 appears twice. However, given the array [1, 2, 3, 4], the function should return false because all elements are distinct.

## Approach
We can solve this problem by using an unordered set to keep track of the elements we have seen so far. We iterate through the array, and for each element, we check if it already exists in the set. If it does, we return true. If it doesn't, we add it to the set. If we finish iterating through the array without finding any duplicates, we return false.

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
            // If the current element already exists in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the current element to the set
            uniqueElements.insert(num);
        }
        // If we finish iterating without finding any duplicates, return false
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
- Use an unordered set to keep track of unique elements in the array.
- Iterate through the array and check for duplicates in O(n) time complexity.
- The space complexity is O(n) because in the worst case, we might need to store all elements in the set.