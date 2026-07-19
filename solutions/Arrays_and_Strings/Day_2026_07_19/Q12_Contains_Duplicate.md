# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array may contain multiple duplicate elements, and the duplicates may be consecutive or non-consecutive. The function should have a time complexity of less than O(n^2) and a space complexity of less than O(n). For example, given the input `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` is duplicated. Given the input `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicates.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over the array, and for each element, it checks if the element is already in the set. If it is, the function returns true. If it's not, the element is added to the set. If the function iterates over the entire array without finding any duplicates, it returns false.

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
        
        // Iterate over the array
        for (int num : nums) {
            // Check if the element is already in the set
            if (uniqueElements.find(num) != uniqueElements.end()) {
                // If it is, return true
                return true;
            }
            // If it's not, add the element to the set
            uniqueElements.insert(num);
        }
        // If the function iterates over the entire array without finding any duplicates, return false
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
- Using an unordered set allows for efficient lookup and insertion of elements with an average time complexity of O(1).
- The algorithm has a time complexity of O(n) because it iterates over the array once.
- The algorithm has a space complexity of O(n) because in the worst-case scenario, it stores all elements from the array in the set.