# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The input will be a single integer n, and the output should be the XOR of all numbers from 0 to n. For example, if n = 3, the output should be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the output should be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4. The range is inclusive, and the numbers are 32-bit integers.

## Approach
The approach to solve this problem is based on the properties of XOR operation and the pattern observed when XORing numbers in a range. We notice that XOR of all numbers from 0 to n follows a pattern based on the least significant bit of n.

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
        // If n is a multiple of 4, the XOR will be n
        if (n % 4 == 0) return n;
        
        // If n is 1 more than a multiple of 4, the XOR will be 1
        if (n % 4 == 1) return 1;
        
        // If n is 2 more than a multiple of 4, the XOR will be n + 1
        if (n % 4 == 2) return n + 1;
        
        // If n is 3 more than a multiple of 4, the XOR will be 0
        return 0;
    }
};
```

## Test Cases
```
Input: 3
Output: 4
Input: 4
Output: 4
Input: 5
Output: 1
Input: 6
Output: 7
Input: 7
Output: 0
```

## Key Takeaways
- The XOR operation has a pattern when applied to a range of numbers.
- By observing the least significant bits of the numbers, we can simplify the calculation of XOR for a range.
- The solution for this problem has a time complexity of O(1), making it efficient for large inputs.