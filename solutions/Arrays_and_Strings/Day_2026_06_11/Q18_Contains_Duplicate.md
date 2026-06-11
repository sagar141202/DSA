# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. A duplicate is an element that appears more than once in the array. The function should return true if any duplicates are found and false otherwise. The array can contain integers ranging from negative to positive, and the size of the array can be up to 10^5 elements. For example, given the array [1, 2, 3, 4, 5], the function should return false, but given the array [1, 2, 3, 2, 5], the function should return true.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates through the array, checking if each element exists in the set. If an element is found in the set, it means a duplicate has been encountered, and the function returns true. If the loop completes without finding any duplicates, the function returns false.

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
        // If the loop completes without finding duplicates, return false
        return false;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4, 5]
Output: false
Input: [1, 2, 3, 2, 5]
Output: true
Input: [1, 1, 1, 1, 1]
Output: true
```

## Key Takeaways
- Using an unordered set allows for efficient lookup and insertion of elements.
- The algorithm has a linear time complexity due to the single pass through the array.
- The space complexity is also linear because in the worst-case scenario, all elements are stored in the set.