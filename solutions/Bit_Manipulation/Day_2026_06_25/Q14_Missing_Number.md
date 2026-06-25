# Missing Number

## Problem Statement
Given an array of integers from 1 to n, where one number is missing, find the missing number. The array is 0-indexed and has a length of n-1. For example, if n = 5, the array could be [1, 2, 4, 5] and the missing number would be 3. The array does not contain duplicates and the numbers are within the range of 1 to n.

## Approach
The approach is to use bitwise XOR operation to find the missing number. We XOR all numbers from 1 to n and all numbers in the array, the result will be the missing number. This works because XOR of a number with itself is 0 and XOR of a number with 0 is the number itself.

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
        int xor_all = 0;
        // XOR all numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        return xor_all;
    }
};
```

## Test Cases
```
Input: [3,0,1]
Output: 2
Input: [0,1]
Output: 2
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The time complexity is O(n) because we need to iterate over all numbers from 1 to n and all numbers in the array.
- The space complexity is O(1) because we only use a constant amount of space to store the result.