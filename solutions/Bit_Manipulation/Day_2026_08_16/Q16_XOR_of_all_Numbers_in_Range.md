# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, and n is a non-negative integer. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 4, and if n = 5, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1.

## Approach
The XOR operation has a useful property: a ^ a = 0 and a ^ 0 = a. We can use this property to find the XOR of all numbers in the range. The idea is to find the pattern of the XOR of all numbers up to a certain point and then use this pattern to calculate the XOR of all numbers in the given range.

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
        // The XOR of all numbers up to n follows a pattern:
        // - If n % 4 == 0, the XOR is n
        // - If n % 4 == 1, the XOR is 1
        // - If n % 4 == 2, the XOR is n + 1
        // - If n % 4 == 3, the XOR is 0
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
Input: n = 5
Output: 1
Input: n = 10
Output: 11
```

## Key Takeaways
- The XOR operation follows a pattern that can be used to simplify the calculation.
- The pattern of the XOR of all numbers up to n can be used to calculate the XOR of all numbers in the given range in constant time.