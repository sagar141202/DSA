# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The function should be able to handle arrays of size up to `10^5` and integers ranging from `-10^9` to `10^9`. For example, given the array `nums = [1, 2, 3, 1]`, the function should return `true` because the element `1` appears twice. However, given the array `nums = [1, 2, 3, 4]`, the function should return `false` because there are no duplicate elements.

## Approach
We can solve this problem by using an unordered set to store the elements we have seen so far. We iterate over the array and for each element, we check if it is already in the set. If it is, we return `true`. If we finish iterating over the array without finding any duplicates, we return `false`. This approach works because looking up an element in a set takes constant time on average.

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
        // Create an empty set to store the elements we have seen
        unordered_set<int> seen;
        
        // Iterate over the array
        for (int num : nums) {
            // If the current element is already in the set, return true
            if (seen.find(num) != seen.end()) {
                return true;
            }
            // Otherwise, add the current element to the set
            seen.insert(num);
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
- Using an unordered set to store the elements we have seen allows us to check for duplicates in constant time on average.
- This approach has a time complexity of O(n) because we are iterating over the array once.
- The space complexity is also O(n) because in the worst case, we might have to store all elements in the set.