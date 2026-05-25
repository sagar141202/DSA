# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array contains all integers from 0 to n, except one. The integers are not guaranteed to be unique. The function should return the missing number. For example, given the array [0, 1, 2, 4], the function should return 3.

## Approach
The solution uses bitwise XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number. This is because XOR of all numbers from 0 to n will have all bits set, and XOR of all numbers in the array will have all bits set except the bit corresponding to the missing number.

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
            res = res ^ i ^ nums[i];
        }
        return res;
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
- The XOR operation can be used to find the missing number in an array.
- The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number.
- This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.