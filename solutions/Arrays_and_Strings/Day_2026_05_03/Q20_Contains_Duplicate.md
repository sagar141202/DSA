# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array may contain multiple duplicates, and the duplicates may be consecutive or non-consecutive. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` is duplicated. However, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicates.

## Approach
We can solve this problem by using an unordered set to store unique elements from the array. We iterate through the array, and for each element, we check if it already exists in the set. If it does, we return `true` because a duplicate has been found. If we iterate through the entire array without finding any duplicates, we return `false`.

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
        // If we've iterated through the entire array without finding any duplicates, return false
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
- We can use an unordered set to efficiently store and look up unique elements in an array.
- The time complexity of this solution is O(n) because we're doing a constant amount of work for each element in the array.
- The space complexity of this solution is also O(n) because in the worst case, we might need to store every element in the array in the set.