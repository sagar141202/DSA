# Number of 1 Bits

## Problem Statement
Write a function that takes an integer as input and returns the number of bits that are set to 1 in its binary representation. The function should be efficient and handle large integers. For example, given the integer 9 (which is 1001 in binary), the function should return 2, because there are two bits set to 1.

## Approach
The approach to solve this problem is to use bit manipulation to count the number of 1 bits in the binary representation of the input integer. We can use a loop to iterate over each bit and increment a counter when a 1 bit is encountered. Alternatively, we can use Brian Kernighan's algorithm, which uses bitwise operations to clear the least significant 1 bit in each iteration.

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
Input: 15
Output: 4
```

## Key Takeaways
- Bit manipulation can be used to solve problems involving binary representations of integers.
- Brian Kernighan's algorithm provides an efficient way to count the number of 1 bits in the binary representation of an integer.
- The time complexity of the solution is O(log n), where n is the input integer, because we iterate over each bit in the binary representation.