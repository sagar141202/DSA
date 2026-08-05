# Missing Number

## Problem Statement
Given an array of integers from 0 to n-1, where n is the length of the array, find the missing number in the array. The array is guaranteed to have one and only one missing number. For example, given the array [0, 1, 3], the missing number is 2. The array can contain duplicates, but the missing number will be in the range [0, n-1]. The function should return the missing number.

## Approach
The approach to solve this problem is to use bitwise XOR operation. We can XOR all numbers in the array and all numbers from 0 to n, and the result will be the missing number. This is because XOR of all numbers from 0 to n will cancel out all numbers that are present in the array, leaving only the missing number.

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
        int result = n;
        for (int i = 0; i < n; i++) {
            result ^= i;
            result ^= nums[i];
        }
        return result;
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
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it suitable for finding the missing number.
- The time complexity is O(n) because we are iterating over the array once.
- The space complexity is O(1) because we are using a constant amount of space to store the result.