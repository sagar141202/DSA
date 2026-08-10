# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents 1, `B` represents 2, and so on. For example, `ZY` would be equivalent to `701` because `Z` represents 26 and `Y` represents 25, so `26 * 26 + 25 = 701`. The input string `s` will only contain uppercase letters.

## Approach
The algorithm involves iterating over the input string from left to right, converting each character to its corresponding number, and calculating the total column number using the base 26 number system. We use the fact that `A` represents 1, `B` represents 2, and so on, to calculate the column number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (char c : s) {
            // Convert character to its corresponding number (A = 1, B = 2, etc.)
            int num = c - 'A' + 1;
            // Calculate the total column number using the base 26 number system
            result = result * 26 + num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: "A"
Output: 1
Input: "AB"
Output: 28
Input: "ZY"
Output: 701
```

## Key Takeaways
- The problem can be solved using the base 26 number system.
- We iterate over the input string from left to right, converting each character to its corresponding number.
- The time complexity is O(n), where n is the length of the input string, because we make a single pass over the string.