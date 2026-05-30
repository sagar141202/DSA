# Missing Number

## Problem Statement
Given an array of integers from 0 to n-1, where each integer appears exactly once, find the missing number in the range [0, n]. The array is guaranteed to have a missing number. The problem can be solved using bit manipulation to find the missing number. For example, if the input array is [0, 1, 3], the output will be 2, which is the missing number in the range [0, 3]. The array can have any size and the missing number can be any integer in the range [0, n].

## Approach
The solution uses XOR operation to find the missing number. The XOR of all numbers from 0 to n is compared with the XOR of all numbers in the array. The result will be the missing number. This approach works because XOR of all numbers from 0 to n is equal to XOR of all numbers in the array and the missing number.

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
        // XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR of all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        // The result will be the missing number
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
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the missing number.
- The time complexity of the solution is O(n) because we need to iterate over all numbers in the array.
- The space complexity of the solution is O(1) because we only use a constant amount of space to store the XOR result.