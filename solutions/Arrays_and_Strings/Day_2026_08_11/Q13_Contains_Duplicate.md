# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should be able to handle arrays of size up to `10^5` and integers in the range `[-10^9, 10^9]`. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. On the other hand, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because all elements are unique.

## Approach
The algorithm uses an unordered set to store the elements of the array as it iterates through them. If an element is already present in the set, it means a duplicate has been found and the function returns `true`. If the function iterates through the entire array without finding any duplicates, it returns `false`. This approach takes advantage of the constant time complexity of set operations in C++.

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
            // If the element is already in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the element to the set
            uniqueElements.insert(num);
        }
        // If no duplicates were found, return false
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
- The space complexity is O(n) because in the worst-case scenario, all elements in the array are unique and must be stored in the set.
- This solution can be easily adapted to solve similar problems involving strings or other data types by modifying the type of the set and the comparison operation.