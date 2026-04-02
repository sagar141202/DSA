# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n (inclusive), calculate the XOR of all numbers in this range. The input will be a single integer n, where 0 <= n <= 10^6. For example, if n = 5, the output should be the XOR of 0, 1, 2, 3, 4, and 5.

## Approach
The XOR of all numbers in a range can be calculated by observing the pattern of XOR operations. We can use the properties of XOR to simplify the calculation. Specifically, we can use the fact that XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
        // If n is a multiple of 4, the XOR is 0 (since each number appears twice)
        if (n % 4 == 0) return n;
        // If n is 1 more than a multiple of 4, the XOR is 1 (since 1 appears once more than all other numbers)
        if (n % 4 == 1) return 1;
        // If n is 2 more than a multiple of 4, the XOR is n + 1 (since n and n+1 appear once more than all other numbers)
        if (n % 4 == 2) return n + 1;
        // If n is 3 more than a multiple of 4, the XOR is 0 (since each number appears twice)
        return 0;
    }
};
```

## Test Cases
```
Input: 5
Output: 1
Input: 10
Output: 11
Input: 7
Output: 0
```

## Key Takeaways
- The XOR of all numbers in a range can be calculated in constant time using the properties of XOR operations.
- The pattern of XOR operations repeats every 4 numbers, so we can use the remainder of n divided by 4 to determine the XOR.
- This solution assumes that the input range is inclusive (i.e., it includes both 0 and n).