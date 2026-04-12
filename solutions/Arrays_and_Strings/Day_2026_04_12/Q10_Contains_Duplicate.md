# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should be able to handle arrays with up to 10^5 elements and integer values ranging from -10^9 to 10^9. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. However, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because all elements are unique.

## Approach
The algorithm uses an unordered set to store unique elements from the array. It iterates over each element in the array, checking if the element already exists in the set. If a duplicate is found, the function immediately returns `true`. If the function iterates over the entire array without finding any duplicates, it returns `false`.

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
            // If the element already exists in the set, return true
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            // Otherwise, add the element to the set
            uniqueElements.insert(num);
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
- Using an unordered set allows for efficient lookup and insertion of elements with an average time complexity of O(1).
- The algorithm has a linear time complexity because it only requires a single pass through the array.
- The space complexity is also linear because in the worst-case scenario, all elements in the array are unique and must be stored in the set.