# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array, and `false` otherwise. The array may contain duplicate elements in any order. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. However, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicate elements.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over the array, checking if each element is already in the set. If an element is found in the set, the function immediately returns `true`. If the function iterates over the entire array without finding any duplicates, it returns `false`.

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
        unordered_set<int> numSet;
        
        // Iterate over the array
        for (int num : nums) {
            // Check if the current element is already in the set
            if (numSet.find(num) != numSet.end()) {
                // If the element is found, return true
                return true;
            }
            // Add the current element to the set
            numSet.insert(num);
        }
        // If no duplicates are found, return false
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
- Using an unordered set allows for efficient lookup of elements in O(1) time.
- The algorithm has a linear time complexity because it only requires a single pass over the input array.
- The space complexity is also linear because in the worst case, the set will store all elements from the input array.