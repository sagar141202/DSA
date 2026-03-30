# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n except one. For example, given the array [0, 1, 3], the missing number is 2. The array is not sorted and may contain duplicates, but the missing number is unique.

## Approach
The approach is to use bitwise XOR operation to find the missing number. The XOR of all numbers from 0 to n is compared with the XOR of all numbers in the array. The result of this comparison gives the missing number.

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
        // XOR all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        // The result is the missing number
        return xor_all;
    }
};
```

## Test Cases
```
Input: [0, 1, 3]
Output: 2
Input: [4, 0, 3, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The time complexity is O(n) because we need to iterate over all numbers from 0 to n and all numbers in the array.
- The space complexity is O(1) because we only use a constant amount of space to store the result.