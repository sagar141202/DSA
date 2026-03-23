# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which can be utilized to simplify the problem. The input range is 0 <= n <= 10^6, and the output should be the XOR of all numbers in the range [0, n].

## Approach
The approach involves utilizing the properties of XOR operation and observing patterns in the XOR of numbers in a range. Specifically, we can observe that the XOR of all numbers up to a certain point can be calculated based on the last two bits of the number.

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
        // If n is a multiple of 4, the XOR will be the same as n % 4
        if (n % 4 == 0) return n;
        // If n % 4 == 1, the XOR will be 1
        if (n % 4 == 1) return 1;
        // If n % 4 == 2, the XOR will be n + 1
        if (n % 4 == 2) return n + 1;
        // If n % 4 == 3, the XOR will be 0
        return 0;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 11
Input: n = 7
Output: 0
```

## Key Takeaways
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which can be utilized to simplify the problem.
- The last two bits of a number determine its contribution to the XOR of all numbers up to that point.
- For any given n, we can calculate the XOR of all numbers in the range [0, n] in constant time using the observed patterns.