# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if we consider the properties of XOR and the pattern it follows for consecutive numbers, we can simplify this problem. We need to write a function that takes an integer n as input and returns the XOR of all numbers from 0 to n.

## Approach
The approach to solve this problem involves understanding the properties of XOR operation and identifying patterns when XOR is applied to consecutive numbers. By analyzing the binary representation of numbers and how XOR works, we can derive a simpler method to calculate the XOR of a range without actually calculating the XOR of each number individually.

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
        // The XOR of all numbers from 0 to n follows a pattern:
        // - If n % 4 == 0, then XOR is n
        // - If n % 4 == 1, then XOR is 1
        // - If n % 4 == 2, then XOR is n + 1
        // - If n % 4 == 3, then XOR is 0
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
Output: 4 is incorrect based on the pattern, the correct output should be 0 because 0 ^ 1 ^ 2 ^ 3 = 0 is incorrect, the correct calculation is 0 ^ 1 ^ 2 ^ 3 = 4 is incorrect. Let's recheck: 0 ^ 1 = 1, 1 ^ 2 = 3, 3 ^ 3 = 0.
Input: n = 4
Output: 4
Input: n = 5
Output: 1
```

## Key Takeaways
- The XOR operation has a pattern when applied to consecutive numbers, which can be used to simplify the calculation.
- The result of XOR of all numbers from 0 to n can be determined by the remainder of n when divided by 4.
- Understanding the properties of bitwise operations can often lead to more efficient solutions for problems involving binary numbers.