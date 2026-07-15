# Counting Bits

## Problem Statement
Given an integer `n`, write a function to count the number of bits that are set (i.e., 1) in the binary representation of all numbers from 0 to `n`. For example, if `n = 5`, the binary representations are: `0 (0b0)`, `1 (0b1)`, `2 (0b10)`, `3 (0b11)`, `4 (0b100)`, `5 (0b101)`. The total number of set bits is `7`. The function should return the total count of set bits.

## Approach
We can iterate over all numbers from 0 to `n`, convert each number to its binary representation, and count the number of set bits. Alternatively, we can use Brian Kernighan's algorithm to count the set bits in each number.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bitset>
using namespace std;

class Solution {
public:
    int countBits(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            // Convert the number to binary and count the set bits
            bitset<32> binary(i);
            count += binary.count();
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 7
Input: n = 15
Output: 22
```

## Key Takeaways
- We can use `bitset` in C++ to easily convert a number to its binary representation and count the set bits.
- Brian Kernighan's algorithm can be used to count the set bits in a number, but it's not necessary for this problem.
- The time complexity is O(n log n) because we're iterating over all numbers up to `n` and converting each number to binary, which takes O(log n) time.