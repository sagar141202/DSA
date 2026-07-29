# Contains Duplicate

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array and return `false` if every element is distinct. The array can contain up to 10^5 integers, and the integers can be in the range of -10^9 to 10^9. For example, given the array `[1, 2, 3, 1]`, the function should return `true` because the number 1 appears twice, but for the array `[1, 2, 3, 4]`, the function should return `false` because all numbers are distinct.

## Approach
We can solve this problem by iterating through the array and keeping track of the elements we have seen. We can use an unordered set to store unique elements. If we encounter an element that is already in the set, we return true, indicating that there is a duplicate. If we finish iterating through the array without finding any duplicates, we return false.

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
            // If the number is already in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the number to the set
            uniqueElements.insert(num);
        }
        // If we finish iterating without finding any duplicates, return false
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
- This solution works for arrays of any size and with any range of integers.