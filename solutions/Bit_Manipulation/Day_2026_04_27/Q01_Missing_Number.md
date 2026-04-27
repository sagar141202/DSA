# Missing Number

## Problem Statement
The problem is to find the missing number in a sequence of numbers from 0 to n. The sequence is represented as an array of integers, and one number is missing from the sequence. The missing number can be any number from 0 to n, where n is the length of the array. For example, if the input array is [0, 1, 3], the missing number is 2. The array will contain distinct integers, and the missing number will be in the range [0, n]. The function should return the missing number.

## Approach
The approach is to use bitwise XOR operation to find the missing number. We can XOR all the numbers in the array and all the numbers from 0 to n, and the result will be the missing number. This works because XOR of all numbers from 0 to n will give us a value, and XOR of all numbers in the array will give us the same value minus the missing number.

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
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the missing number.
- The time complexity of the solution is O(n), where n is the length of the array, because we need to iterate over all numbers from 0 to n and all numbers in the array.
- The space complexity of the solution is O(1), because we only need a constant amount of space to store the result.