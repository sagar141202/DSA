# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n (inclusive), find the XOR of all numbers in this range. The input will be a single integer n, and the output should be the XOR of all numbers from 0 to n. For example, if n = 3, the output should be 0 ^ 1 ^ 2 ^ 3 = 4, and if n = 5, the output should be 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1. The range of n is from 0 to 10^6.

## Approach
The approach to solve this problem is to use the properties of XOR operation. We can observe that XOR of all numbers from 0 to n can be calculated using a simple formula based on the last two bits of n. If n is even, the XOR will be the same as the XOR of numbers from 0 to n-1. If n is odd, the XOR will be n XOR the XOR of numbers from 0 to n-1.

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
        // If n is a multiple of 4, the XOR will be n
        if (n % 4 == 0) return n;
        // If n is 1 more than a multiple of 4, the XOR will be 1
        if (n % 4 == 1) return 1;
        // If n is 2 more than a multiple of 4, the XOR will be n+1
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
Input: 5
Output: 1
Input: 10
Output: 11
```

## Key Takeaways
- The XOR operation has a periodic pattern of 4: 0, 1, n+1, 0.
- We can use this pattern to calculate the XOR of all numbers in the range from 0 to n in constant time.
- This solution works for any positive integer n, and it does not require any loops or recursive calls.