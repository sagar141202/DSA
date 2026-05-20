# Excel Sheet Column Number

## Problem Statement
Given a string `s` which represents the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. For example, `A` is 1, `B` is 2, `Z` is 26, `AA` is 27, `AB` is 28, and so on.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number, where `A` represents 1, `B` represents 2, and so on. We can then convert this base-26 number to a decimal number.

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
            // Calculate the value of the current character and add it to the result
            result = result * 26 + (c - 'A' + 1);
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
- The Excel column title can be treated as a base-26 number.
- The conversion from base-26 to decimal can be done by multiplying the current result by 26 and adding the value of the current character.
- The value of the current character can be calculated by subtracting the ASCII value of 'A' from the ASCII value of the character and adding 1.