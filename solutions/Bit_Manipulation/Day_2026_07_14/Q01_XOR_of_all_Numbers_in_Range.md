# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the result would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4, because 4 is not changed by the XOR operation with the previous numbers.

## Approach
The algorithm involves using the properties of XOR operation to find patterns in the range. We can use the fact that XOR of all numbers from 0 to n can be calculated using the properties of even and odd numbers. Specifically, for even n, the result is n, and for odd n, the result is 0 if n is a multiple of 4, and n otherwise, but considering the XOR of the range 0 to n, a pattern emerges where the result depends on the last two bits of n.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorRange(int n) {
        // calculate XOR for the range 0 to n
        if (n % 4 == 0) return n;
        if (n % 4 == 1) return 1;
        if (n % 4 == 2) return n + 1;
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
- The XOR operation has a pattern when applied to a range of numbers from 0 to n, which can be exploited to simplify the calculation.
- The result depends on the last two bits of n, which determines whether n is a multiple of 4 or not, and whether it's even or odd.
- The solution has a constant time complexity because it only involves a fixed number of operations regardless of the input size n.