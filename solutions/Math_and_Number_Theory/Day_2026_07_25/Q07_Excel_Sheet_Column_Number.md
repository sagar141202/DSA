# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing a column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The same letter may appear more than once in the title, and the title can be at most 7 characters long. For example, `AB` corresponds to the column number `28` because `A` is the first column and `B` is the second column.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number, where each digit is represented by a letter from `A` to `Z`. We can then convert this base-26 number to a decimal number.

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
- Each character in the title can be converted to its corresponding decimal value by subtracting the ASCII value of 'A' and adding 1.
- The result can be calculated by multiplying the current result by 26 and adding the value of the current character.