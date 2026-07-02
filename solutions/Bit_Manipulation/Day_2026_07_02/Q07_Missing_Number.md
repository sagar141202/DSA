# Missing Number

## Problem Statement
Given an array of integers from 0 to n-1, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n-1 except one, which is missing. The integers in the array are not guaranteed to be unique. The missing number can be any integer from 0 to n. For example, given the array [0, 1, 2, 4], the missing number is 3. Given the array [0, 2, 3], the missing number is 1.

## Approach
The approach is to use bit manipulation to find the missing number. We can use XOR operation to find the missing number. The XOR of all numbers from 0 to n is equal to the XOR of all numbers in the array and the missing number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int res = n;
        for (int i = 0; i < n; i++) {
            // XOR of all numbers from 0 to n
            res = res ^ i ^ nums[i];
        }
        return res;
    }
};
```

## Test Cases
```
Input: [0, 1, 2, 4]
Output: 3
Input: [0, 2, 3]
Output: 1
```

## Key Takeaways
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the missing number.
- The time complexity is O(n) because we need to iterate over the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the result.