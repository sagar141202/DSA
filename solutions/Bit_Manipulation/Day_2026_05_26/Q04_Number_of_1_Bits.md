# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of 0 to 4294967295 (2^32 - 1). For example, the binary representation of 9 is 1001, so the function should return 2.

## Approach
The approach is to use bitwise operations to count the number of 1 bits in the binary representation of the input integer. We can use a loop to iterate over each bit in the integer and increment a counter whenever we encounter a 1 bit. The algorithm can be optimized by using Brian Kernighan's algorithm, which removes the least significant 1 bit in each iteration.

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
            // Brian Kernighan's algorithm: n & (n - 1) removes the least significant 1 bit
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
- Brian Kernighan's algorithm is an efficient way to count the number of 1 bits in an integer's binary representation.
- The time complexity of the algorithm is O(log n), where n is the input integer, because we are iterating over each bit in the integer.