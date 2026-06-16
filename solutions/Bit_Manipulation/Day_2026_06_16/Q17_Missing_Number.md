# Missing Number

## Problem Statement
The problem is to find the missing number in an array of integers from 0 to n, where n is the size of the array. The array contains all integers from 0 to n except one. For example, if the input array is [0, 1, 3], the missing number is 2. The function should take an array of integers as input and return the missing number. The array can contain duplicate numbers, but the missing number will always be unique.

## Approach
The approach is to use bitwise XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number. This is because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
        // calculate XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        // calculate XOR of all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        // the missing number is the XOR of all numbers
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
- The XOR operation can be used to find the missing number in an array of integers.
- The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number.
- The time complexity of the solution is O(n), where n is the size of the array.