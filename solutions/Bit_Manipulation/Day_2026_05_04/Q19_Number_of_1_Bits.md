# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer will be in the range [0, 2^32 - 1]. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 13 is 1101, so the function should return 3.

## Approach
The approach is to use bitwise operations to count the number of 1 bits in the binary representation of the input integer. We can use a loop to iterate over each bit in the integer and increment a counter whenever we encounter a 1 bit. Alternatively, we can use Brian Kernighan's algorithm, which is more efficient.

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
            // clear the least significant 1 bit
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
Input: 13
Output: 3
```

## Key Takeaways
- The binary representation of an integer can be manipulated using bitwise operations.
- Brian Kernighan's algorithm is an efficient way to count the number of 1 bits in the binary representation of an integer.
- The time complexity of the solution is O(log n) because we are iterating over the bits of the input integer, and the number of bits is proportional to the logarithm of the integer.