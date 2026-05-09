# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array may contain duplicate elements, and the function should be case-sensitive for string inputs. For example, given the array `nums = [1,2,3,1]`, the function should return `true` because the element `1` appears twice in the array. On the other hand, given the array `nums = [1,2,3,4]`, the function should return `false` because all elements in the array are unique. The size of the input array is in the range `[1, 105]`, and the elements of the array are in the range `[0, 105]`.

## Approach
The approach to solve this problem is to use an unordered set data structure to store unique elements from the input array. We iterate over the array, and for each element, we check if it already exists in the set. If it does, we return `true` as we have found a duplicate element. If we iterate over the entire array without finding any duplicates, we return `false`.

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
        
        // Iterate over the input array
        for (int num : nums) {
            // Check if the current element already exists in the set
            if (uniqueElements.find(num) != uniqueElements.end()) {
                // If it does, return true as we have found a duplicate element
                return true;
            }
            // If not, add the current element to the set
            uniqueElements.insert(num);
        }
        // If we have iterated over the entire array without finding any duplicates, return false
        return false;
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: true
Input: nums = [1,2,3,4]
Output: false
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Key Takeaways
- We can use an unordered set to keep track of unique elements in the array.
- The time complexity of this solution is O(n) because we are iterating over the array once.
- The space complexity is also O(n) because in the worst-case scenario, we may need to store all elements in the set.