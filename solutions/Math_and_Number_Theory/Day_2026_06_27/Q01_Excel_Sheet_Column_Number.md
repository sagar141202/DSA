# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The column title can contain multiple characters. For example, `AA` represents the 27th column, `AB` represents the 28th column, and `AZ` represents the 52nd column.

## Approach
The approach is to treat the Excel column title as a base-26 number, where `A` represents 1, `B` represents 2, and so on. We can then convert this base-26 number to a decimal number.

## Complexity
- Time: O(n), where n is the length of the string `s`
- Space: O(1), as we only use a constant amount of space

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (char c : s) {
            // Convert the character to its corresponding number (A = 1, B = 2, etc.)
            int num = c - 'A' + 1;
            // Multiply the current result by 26 and add the new number
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
Input: "AZ"
Output: 52
Input: "AA"
Output: 27
```

## Key Takeaways
- The Excel column title can be treated as a base-26 number.
- We can convert the base-26 number to a decimal number by multiplying the current result by 26 and adding the new number.
- The time complexity is O(n), where n is the length of the string `s`, because we iterate over the string once.