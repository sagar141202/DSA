# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in the binary representation of the integer. The function should be efficient and handle large inputs. For example, the binary representation of the integer 9 is 1001, which has 2 bits that are 1. The function should return 2 for the input 9. The input will be in the range [0, 2^32 - 1].

## Approach
The algorithm uses bit manipulation to count the number of 1 bits in the binary representation of the integer. It works by shifting the bits of the integer to the right and checking the least significant bit. If the least significant bit is 1, it increments the count. The process is repeated until all bits have been checked.

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
            // if the least significant bit is 1, increment the count
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
- Use bit manipulation to count the number of 1 bits in the binary representation of an integer.
- The time complexity is O(log n) because the number of bits in the binary representation of an integer is proportional to the logarithm of the integer.
- The space complexity is O(1) because the algorithm only uses a constant amount of space to store the count and the input integer.