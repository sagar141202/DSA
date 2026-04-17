# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach to solve this problem is to use bit manipulation to count the number of 1 bits in the binary representation of the input integer. We can use a loop to iterate over each bit in the integer and use a bitwise AND operation to check if the bit is 1. If the bit is 1, we increment a counter variable.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {
            // use bitwise AND operation to check if the least significant bit is 1
            count += n & 1;
            // use bitwise right shift operation to move to the next bit
            n >>= 1;
        }
        return count;
    }
};
```

## Test Cases
```
Input: 9
Output: 2
Input: 15
Output: 4
```

## Key Takeaways
- Use bit manipulation to count the number of 1 bits in the binary representation of an integer.
- Use a loop to iterate over each bit in the integer and use a bitwise AND operation to check if the bit is 1.
- Use a bitwise right shift operation to move to the next bit in the integer.