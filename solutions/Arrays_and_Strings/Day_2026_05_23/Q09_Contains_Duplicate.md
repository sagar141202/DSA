# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array may contain duplicate elements in any order, and the function should return as soon as a duplicate is found. The input array `nums` will contain only integers, and the size of the array `n` will be in the range `[1, 10^5]`. For example, given the input `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. On the other hand, given the input `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicate elements.

## Approach
The algorithm uses an unordered set to store unique elements encountered so far. It iterates through the input array, checking if each element is already present in the set. If a duplicate element is found, the function immediately returns `true`. If the entire array is traversed without finding any duplicates, the function returns `false`.

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
        
        // Iterate through the input array
        for (int num : nums) {
            // Check if the current element is already in the set
            if (uniqueElements.find(num) != uniqueElements.end()) {
                // If the element is already in the set, return true (duplicate found)
                return true;
            }
            // Add the current element to the set
            uniqueElements.insert(num);
        }
        // If the entire array is traversed without finding any duplicates, return false
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
- Use an unordered set to efficiently store and look up unique elements.
- Iterate through the input array and check for duplicates by looking up each element in the set.
- Return as soon as a duplicate is found to minimize unnecessary iterations.