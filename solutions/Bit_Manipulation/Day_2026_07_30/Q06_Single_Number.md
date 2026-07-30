# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array can contain duplicate values and the single number can be any value (positive, negative, or zero). The array size will be between 1 and 10000. For example, if the input is [2, 2, 1], the output should be 1 because 1 appears only once in the array. If the input is [4, 1, 2, 1, 2], the output should be 4.

## Approach
The algorithm uses bitwise XOR operation to find the single number. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself. By XORing all numbers in the array, the numbers that appear twice will cancel out, leaving the single number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        // XOR all numbers in the array
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2, 2, 1]
Output: 1
Input: [4, 1, 2, 1, 2]
Output: 4
Input: [1]
Output: 1
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has a time complexity of O(n) and a space complexity of O(1), making it efficient for large arrays.
- This solution works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.