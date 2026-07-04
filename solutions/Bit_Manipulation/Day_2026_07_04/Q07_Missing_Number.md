# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where one number is missing, find the missing number. The array is of size n and contains distinct integers. For example, if the input array is [0, 1, 3], the output should be 2, because 2 is the missing number in the sequence from 0 to 3. The array can contain negative numbers and the missing number can be any number in the range from the smallest to the largest number in the array.

## Approach
We can use bitwise XOR operation to find the missing number, as XOR of all numbers from 0 to n and XOR of all numbers in the array will give us the missing number. This approach works because XOR of a number with itself is 0 and XOR of a number with 0 is the number itself.

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
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The time complexity of this solution is O(n) because we are iterating over the array and the range of numbers from 0 to n.
- The space complexity of this solution is O(1) because we are using a constant amount of space to store the result.