# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should have a time complexity of less than O(n^2) and a space complexity of less than O(n). For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. Given the array `nums = [1, 2, 3, 4]`, the function should return `false` because all elements are unique.

## Approach
The algorithm uses an unordered set to store the elements we have seen so far. We iterate through the array and for each element, we check if it already exists in the set. If it does, we return `true` because we have found a duplicate. If we finish iterating through the array without finding any duplicates, we return `false`.

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
            // Otherwise, add the element to the set
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
- Using an unordered set allows us to check for duplicates in O(1) time on average.
- The overall time complexity of the solution is O(n) because we are iterating through the array once.
- The space complexity is also O(n) because in the worst case, we might have to store all elements in the set.