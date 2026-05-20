# Contains Duplicate

## Problem Statement
Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise. The array contains only integers and the integers are within the range `[0, 10^5]`. The size of the array is within the range `[0, 10^4]`. For example, given `nums = [1,2,3,1]`, the function should return `true` because there are duplicate elements in the array. Given `nums = [1,2,3,4]`, the function should return `false` because there are no duplicate elements in the array.

## Approach
We can solve this problem by using an unordered set to store the elements of the array as we iterate over it. If we encounter an element that is already in the set, we immediately return `true`. If we finish iterating over the array without finding any duplicates, we return `false`. This approach works because an unordered set in C++ has an average time complexity of O(1) for insertion and search operations.

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
        // Create an unordered set to store the elements of the array
        unordered_set<int> numSet;
        
        // Iterate over the array
        for (int num : nums) {
            // If the current element is already in the set, return true
            if (numSet.find(num) != numSet.end()) {
                return true;
            }
            // Otherwise, add the current element to the set
            numSet.insert(num);
        }
        // If we finish iterating over the array without finding any duplicates, return false
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
- Using an unordered set can greatly improve the efficiency of the solution by reducing the time complexity of insertion and search operations.
- This solution has a time complexity of O(n) because we are iterating over the array once.
- This solution has a space complexity of O(n) because in the worst case, we may need to store all elements of the array in the set.