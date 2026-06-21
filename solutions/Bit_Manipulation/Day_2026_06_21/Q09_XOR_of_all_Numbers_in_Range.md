# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n (inclusive), find the XOR of all numbers in this range. The XOR operation has the following properties: a ^ a = 0, a ^ 0 = a, and a ^ b = b ^ a. For example, if n = 5, the XOR of all numbers in the range is 0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1.

## Approach
The XOR of all numbers in a range can be calculated using the properties of XOR operation and pattern observation. We can observe that the XOR of all numbers from 0 to n follows a pattern: if n is a multiple of 4, the result is n; if n % 4 == 1, the result is 1; if n % 4 == 2, the result is n + 1; if n % 4 == 3, the result is 0.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int xorOfRange(int n) {
    // if n is a multiple of 4, the result is n
    if (n % 4 == 0) return n;
    // if n % 4 == 1, the result is 1
    if (n % 4 == 1) return 1;
    // if n % 4 == 2, the result is n + 1
    if (n % 4 == 2) return n + 1;
    // if n % 4 == 3, the result is 0
    return 0;
}
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 10
Input: n = 7
Output: 0
```

## Key Takeaways
- The XOR operation has the properties of commutativity, associativity, and distributivity.
- The XOR of all numbers in a range can be calculated using pattern observation and the properties of XOR operation.
- The time complexity of this solution is O(1), making it efficient for large inputs.