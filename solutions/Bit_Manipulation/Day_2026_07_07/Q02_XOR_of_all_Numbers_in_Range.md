# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The XOR operation has a property that a ^ a = 0 and a ^ 0 = a. We can use this property to simplify the problem. For example, if n = 3, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 = 1. If n = 4, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4. The range is 0-indexed and 0 <= n <= 10^6.

## Approach
We can use the property of XOR to simplify the problem. The XOR of all numbers from 0 to n can be calculated by considering the bits of the numbers. We can iterate over each bit position and calculate the XOR of the numbers at that position.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfAllNumbersInRange(int n) {
        // If n is even, the XOR is n
        if (n % 2 == 0) {
            return n;
        } 
        // If n is odd, the XOR is 1
        else {
            return 1 ^ (n - 1);
        }
    }
};
```

## Test Cases
```
Input: n = 3
Output: 1
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which can be used to simplify the problem.
- We can use bit manipulation to calculate the XOR of all numbers in the range.
- The time complexity of the solution is O(log n) due to the iteration over each bit position.