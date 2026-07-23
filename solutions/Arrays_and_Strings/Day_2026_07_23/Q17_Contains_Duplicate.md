# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should be able to handle arrays of size up to 10^5 and integers in the range [-10^9, 10^9]. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. On the other hand, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicate elements.

## Approach
We can solve this problem by iterating over the array and inserting each element into a set. If we encounter an element that is already in the set, we return `true` because we have found a duplicate. If we finish iterating over the array without finding any duplicates, we return `false`. This approach works because sets in C++ have an average time complexity of O(1) for insertions and lookups.

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
        // Create an empty set to store unique elements
        unordered_set<int> uniqueElements;
        
        // Iterate over the array
        for (int num : nums) {
            // If the current element is already in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, insert the current element into the set
            uniqueElements.insert(num);
        }
        // If we finish iterating over the array without finding any duplicates, return false
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
- Use a set to keep track of unique elements in the array.
- Iterate over the array and check if each element is already in the set.
- If a duplicate element is found, return true immediately.
- If no duplicates are found after iterating over the entire array, return false.