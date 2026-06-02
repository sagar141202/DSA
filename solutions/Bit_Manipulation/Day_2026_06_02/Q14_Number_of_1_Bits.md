# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 11 is 1011, so the function should return 3. The binary representation of 128 is 10000000, so the function should return 1.

## Approach
The approach is to use bitwise operations to count the number of 1 bits in the binary representation of the input integer. We can use a loop to repeatedly clear the least significant 1 bit and increment the count. The algorithm will terminate when all 1 bits have been cleared.

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
Input: 11
Output: 3
Input: 128
Output: 1
```

## Key Takeaways
- Use bitwise operations to manipulate the binary representation of integers.
- The expression `n & (n - 1)` can be used to clear the least significant 1 bit in the binary representation of `n`.
- The time complexity of the algorithm is O(log n) because we are effectively dividing the input by 2 in each iteration.