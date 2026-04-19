# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. A duplicate is an element that appears more than once in the array. The function should return true if any duplicates are found and false otherwise. The array can contain up to 10^5 elements, and each element can be in the range of -10^9 to 10^9. For example, the array [1, 2, 3, 4, 5] does not contain any duplicates, but the array [1, 2, 3, 2, 5] does.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over each element in the array and checks if it already exists in the set. If it does, the function returns true, indicating a duplicate. If it doesn't, the element is added to the set. This approach ensures a fast lookup time and efficient storage of unique elements.

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
        
        // Iterate over each element in the array
        for (int num : nums) {
            // Check if the element already exists in the set
            if (uniqueElements.find(num) != uniqueElements.end()) {
                // If it does, return true, indicating a duplicate
                return true;
            }
            // If it doesn't, add the element to the set
            uniqueElements.insert(num);
        }
        // If no duplicates are found, return false
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
- Use an unordered set for fast lookup and efficient storage of unique elements.
- Iterate over the array and check for duplicates in a single pass.
- Return as soon as a duplicate is found for optimal performance.