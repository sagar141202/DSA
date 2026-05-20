# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The solution should have a linear time complexity and use a constant amount of extra space. For example, if the input is `[2, 2, 1]`, the function should return `1` because `1` appears only once in the array. If the input is `[4, 1, 2, 1, 2]`, the function should return `4` because `4` appears only once in the array.

## Approach
The algorithm uses bit manipulation to find the single number. It initializes a variable `result` to 0 and then iterates over each number in the array, performing a bitwise XOR operation between `result` and the current number. This works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
        // iterate over each number in the array
        for (int num : nums) {
            // perform a bitwise XOR operation between result and the current number
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
```

## Key Takeaways
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the single number in the array.
- The solution has a linear time complexity because it only needs to iterate over the array once.
- The solution uses a constant amount of extra space because it only uses a single variable to store the result.