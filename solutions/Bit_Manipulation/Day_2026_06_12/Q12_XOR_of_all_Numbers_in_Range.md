# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4 as well because 4 is a special case where the XOR result is always the same as the highest power of 2 minus 1 that is less than or equal to n. The goal is to write an efficient algorithm that can compute this XOR for any given n.

## Approach
The approach involves understanding the properties of XOR operation and its pattern when applied to a range of numbers. Specifically, recognizing that XOR of all numbers up to n can be simplified by examining the pattern of XOR results for different ranges and leveraging the properties of binary representation.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfRange(int n) {
        // If n is a multiple of 4, then the result is n
        if (n % 4 == 0) return n;
        // If n is 1 more than a multiple of 4, then the result is 1
        if (n % 4 == 1) return 1;
        // If n is 2 more than a multiple of 4, then the result is n + 1
        if (n % 4 == 2) return n + 1;
        // If n is 3 more than a multiple of 4, then the result is 0
        return 0;
    }
};
```

## Test Cases
```
Input: n = 3
Output: 4
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation has a specific pattern when applied to a range of consecutive numbers.
- Recognizing this pattern allows for an efficient solution that avoids iterating over the entire range.
- The solution leverages the properties of binary representation and modular arithmetic to simplify the computation.