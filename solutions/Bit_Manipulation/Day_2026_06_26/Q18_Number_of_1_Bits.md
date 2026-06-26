# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The function should be efficient and handle large inputs.

## Approach
The approach is to use bitwise operations to iterate over each bit in the binary representation of the input integer. We will use a while loop to shift the bits of the integer to the right and count the number of 1 bits. The algorithm will terminate when all bits have been processed.

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
            // count the least significant 1 bit
            count += n & 1;
            // shift the bits to the right
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
- Use bitwise operations to efficiently process the binary representation of an integer.
- The time complexity is O(log n) because we are shifting the bits to the right in each iteration, effectively reducing the number of bits by half.
- The space complexity is O(1) because we only use a constant amount of space to store the count of 1 bits.