# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We need to find the XOR of all numbers from 0 to n. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR is 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4.

## Approach
We can solve this problem by observing the pattern of XOR of numbers from 0 to n. If n is a multiple of 4, the XOR is n. If n is of the form 4k + 1, the XOR is 1. If n is of the form 4k + 2, the XOR is n + 1. If n is of the form 4k + 3, the XOR is 0.

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
        // If n is a multiple of 4, the XOR is n
        if (n % 4 == 0) return n;
        // If n is of the form 4k + 1, the XOR is 1
        else if (n % 4 == 1) return 1;
        // If n is of the form 4k + 2, the XOR is n + 1
        else if (n % 4 == 2) return n + 1;
        // If n is of the form 4k + 3, the XOR is 0
        else return 0;
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
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a.
- The pattern of XOR of numbers from 0 to n can be observed and used to solve the problem in O(1) time complexity.
- The solution can be implemented using simple conditional statements in C++.