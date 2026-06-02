# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. A duplicate is an element that appears more than once in the array. The function should return true if any duplicates are found and false otherwise. The array can contain integers of any value, positive, negative, or zero, and can be of any size. For example, given the array [1, 2, 3, 4, 5], the function should return false, while given the array [1, 2, 3, 2, 5], the function should return true.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over the array and checks if each element is already in the set. If an element is found in the set, it means a duplicate has been found, and the function returns true. If the function iterates over the entire array without finding any duplicates, it returns false.

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
        unordered_set<int> unique_nums;
        
        // Iterate over the array
        for (int num : nums) {
            // If the number is already in the set, return true
            if (unique_nums.find(num) != unique_nums.end()) {
                return true;
            }
            // Otherwise, add the number to the set
            unique_nums.insert(num);
        }
        // If no duplicates are found, return false
        return false;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 1]
Output: true
Input: [1, 2, 3, 4]
Output: false
Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

## Key Takeaways
- Use of an unordered set to store unique elements allows for efficient lookup and insertion of elements.
- The algorithm has a time complexity of O(n) because it makes a single pass over the array, and the space complexity is also O(n) because in the worst case, the set will store all elements from the array.