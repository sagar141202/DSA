# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array, and `false` otherwise. The function should be able to handle arrays of size up to `10^5` and integer values up to `10^9`. For example, given the array `[1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. However, given the array `[1, 2, 3, 4]`, the function should return `false` because all elements are unique.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over the array and checks if each element is already in the set. If an element is found in the set, the function immediately returns `true`. If the function iterates over the entire array without finding any duplicates, it returns `false`.

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
            // Check if the current element is already in the set
            if (uniqueElements.find(num) != uniqueElements.end()) {
                // If the element is found, return true
                return true;
            }
            // If not, add the element to the set
            uniqueElements.insert(num);
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
- Using an unordered set allows for efficient lookup and insertion of elements, resulting in a time complexity of O(n).
- The space complexity is also O(n) because in the worst case, all elements in the array are unique and stored in the set.
- This solution can handle large arrays and integer values, making it suitable for a wide range of inputs.