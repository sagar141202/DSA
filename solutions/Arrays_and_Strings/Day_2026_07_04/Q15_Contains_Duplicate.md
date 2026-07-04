# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should be able to handle arrays of size up to 10^5 and integers in the range [-10^9, 10^9]. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. On the other hand, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicate elements.

## Approach
The approach to solve this problem is to use an unordered set to store unique elements from the array. We iterate over the array, and for each element, we check if it already exists in the set. If it does, we return `true` because we have found a duplicate. If we finish iterating over the array without finding any duplicates, we return `false`.

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
        unordered_set<int> unique_elements;
        
        // Iterate over the array
        for (int num : nums) {
            // Check if the current element already exists in the set
            if (unique_elements.find(num) != unique_elements.end()) {
                // If it does, return true because we have found a duplicate
                return true;
            }
            // If not, add the current element to the set
            unique_elements.insert(num);
        }
        // If we finish iterating over the array without finding any duplicates, return false
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
- Using an unordered set allows us to check for duplicates in constant time on average.
- The space complexity is linear because in the worst case, we might need to store all elements from the array in the set.
- This solution works for arrays of any size and with integers in any range.