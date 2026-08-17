# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, which has 2 bits that are 1, and the binary representation of 15 is 1111, which has 4 bits that are 1.

## Approach
The approach involves using bitwise operations to count the number of 1 bits. We can use Brian Kernighan's algorithm, which works by subtracting the least significant 1 bit from the number in each iteration. This process is repeated until all bits become 0. The number of iterations required to make all bits 0 is equal to the number of 1 bits in the original number.

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
            // subtract the least significant 1 bit from n
            n &= (n - 1);
            count++;
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
- Use bitwise operations to solve bit manipulation problems efficiently.
- Brian Kernighan's algorithm can be used to count the number of 1 bits in a binary representation.
- The time complexity of this solution is O(log n) because we are essentially counting the number of bits in the binary representation of n.