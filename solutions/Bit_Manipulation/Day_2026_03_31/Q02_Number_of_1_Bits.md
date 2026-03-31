# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer will be in the range [0, 2^32 - 1]. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bitwise operations to count the number of 1 bits in the binary representation of the input integer. We can use a while loop to iterate over each bit in the integer. In each iteration, we check if the least significant bit is 1 and increment the count if it is. Then, we right shift the integer by 1 bit to move to the next bit.

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
            // check if the least significant bit is 1
            count += n & 1;
            // right shift the integer by 1 bit
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
- Use bitwise operations to manipulate individual bits in an integer.
- The expression `n & 1` checks if the least significant bit of `n` is 1.
- The expression `n >>= 1` right shifts the integer `n` by 1 bit.