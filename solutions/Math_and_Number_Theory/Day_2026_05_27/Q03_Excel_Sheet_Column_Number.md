# Excel Sheet Column Number

## Problem Statement
Given a string `columnTitle` representing the column title as it appears in an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A = 1`, `B = 2`, ..., `Z = 26`, `AA = 27`, `AB = 28`, ..., `AZ = 52`, `BA = 53`, and so on. For example, if `columnTitle = "A"`, the output should be `1`. If `columnTitle = "AB"`, the output should be `28`. If `columnTitle = "ZY"`, the output should be `701`.

## Approach
The approach to solve this problem is to treat the Excel column title as a base-26 number, where each character represents a digit in the range `[A, Z]`. We can then convert this base-26 number to a decimal number. The algorithm iterates over the input string from left to right, calculating the decimal value of each character and adding it to the total sum after multiplying it by the appropriate power of 26.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        for (char c : columnTitle) {
            // subtract 'A' - 1 to get the value of the character (A = 1, B = 2, etc.)
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: columnTitle = "A"
Output: 1
Input: columnTitle = "AB"
Output: 28
Input: columnTitle = "ZY"
Output: 701
```

## Key Takeaways
- The problem can be solved by treating the Excel column title as a base-26 number.
- The time complexity is linear with respect to the length of the input string.
- The space complexity is constant, as we only use a fixed amount of space to store the result.