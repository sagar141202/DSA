# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array may contain duplicate elements in any order, and the size of the array can range from 1 to 10^5. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice, and given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicate elements.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates through the array, and for each element, it checks if the element is already in the set. If the element is in the set, the function immediately returns `true`. If the element is not in the set, it is added to the set. If the function iterates through the entire array without finding any duplicate elements, it returns `false`.

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
        
        // Iterate through the array
        for (int num : nums) {
            // If the element is already in the set, return true
            if (numSet.find(num) != numSet.end()) {
                return true;
            }
            // If the element is not in the set, add it to the set
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
- Use an unordered set to store unique elements for efficient lookup.
- Iterate through the array only once to achieve a time complexity of O(n).
- The space complexity is O(n) because in the worst case, all elements in the array are unique and stored in the set.