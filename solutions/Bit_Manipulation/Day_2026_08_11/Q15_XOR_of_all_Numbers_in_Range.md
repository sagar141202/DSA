# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR is 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4.

## Approach
The algorithm uses the property of XOR that a ^ a = 0 and a ^ 0 = a. We can observe a pattern where the XOR of all numbers up to n is the same as the XOR of all numbers up to n-1 if n is even, and the XOR of all numbers up to n-1 XOR n if n is odd.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfAllNumbersInRange(int n) {
        // If n is a multiple of 4, the result is n
        if (n % 4 == 0) return n;
        
        // If n is 1 more than a multiple of 4, the result is 1
        if (n % 4 == 1) return 1;
        
        // If n is 2 more than a multiple of 4, the result is n + 1
        if (n % 4 == 2) return n + 1;
        
        // If n is 3 more than a multiple of 4, the result is 0
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
- The XOR of all numbers up to n follows a repeating pattern of length 4.
- We can use the modulo operator to determine which part of the pattern n falls into.
- The result can be calculated in constant time using a simple formula based on the remainder of n divided by 4.