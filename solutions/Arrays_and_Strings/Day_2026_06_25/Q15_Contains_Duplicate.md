# Contains Duplicate

## Problem Statement
Given an array of integers, determine if the array contains any duplicates. A duplicate is an element that appears more than once in the array. The function should return true if any duplicates are found and false otherwise. The array can contain any type of integer (positive, negative, or zero) and can be of any size. For example, given the array [1, 2, 3, 4, 5], the function should return false because there are no duplicates, but given the array [1, 2, 3, 2, 5], the function should return true because the number 2 is duplicated.

## Approach
We can use an unordered set to keep track of the elements we've seen so far. We iterate through the array, and for each element, we check if it's already in the set. If it is, we return true because we've found a duplicate. If we get through the entire array without finding any duplicates, we return false.

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
        
        // Iterate through the array
        for (int num : nums) {
            // If the number is already in the set, return true
            if (unique_nums.find(num) != unique_nums.end()) {
                return true;
            }
            // Otherwise, add the number to the set
            unique_nums.insert(num);
        }
        // If we get through the entire array without finding any duplicates, return false
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
- Using an unordered set allows us to check for duplicates in constant time.
- The space complexity is O(n) because in the worst-case scenario, we might have to store all elements in the set.
- This solution works for arrays of any size and can contain any type of integer.