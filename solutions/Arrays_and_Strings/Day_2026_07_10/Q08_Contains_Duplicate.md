# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should be able to handle arrays of size up to `10^5` and integers in the range `[-10^9, 10^9]`. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` is duplicated. On the other hand, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicates.

## Approach
The approach to solve this problem is to use an unordered set to store the elements of the array as we iterate through it. If we encounter an element that is already in the set, we immediately return `true` because a duplicate has been found. If we iterate through the entire array without finding any duplicates, we return `false`.

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
        // If we've iterated through the entire array without finding duplicates, return false
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
- Using an unordered set allows for efficient lookup and insertion of elements, making the solution scalable for large arrays.
- The time complexity of O(n) is achieved because in the worst case, we need to iterate through the entire array.
- The space complexity of O(n) is due to the storage required for the unordered set in the worst case when all elements are unique.