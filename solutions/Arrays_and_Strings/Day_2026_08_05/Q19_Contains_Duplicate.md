# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array, and `false` otherwise. The function should be able to handle arrays with up to 10^5 elements and integers in the range [-10^9, 10^9]. For example, given the array `[1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice, while for the array `[1, 2, 3, 4]`, the function should return `false` because there are no duplicates.

## Approach
The solution uses an unordered set to store unique elements from the array. It iterates over the array, adding each element to the set. If an element is already present in the set, it means a duplicate has been found, and the function returns `true`. If the loop completes without finding any duplicates, the function returns `false`.

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
Input: [1, 2, 3, 1]
Output: true
Input: [1, 2, 3, 4]
Output: false
Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
```

## Key Takeaways
- Using an unordered set allows for efficient lookups and insertions, making the solution scalable for large inputs.
- The solution has a linear time complexity because it only requires a single pass through the input array.