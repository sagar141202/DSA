# Excel Sheet Column Number

## Problem Statement
Given a string `columnTitle` representing the column title as it appears in an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The column title can contain multiple characters, for example, "AA" represents the 27th column. The input string will always be a valid Excel column title.

## Approach
The approach is to treat the Excel column title as a base-26 number system where 'A' represents 1, 'B' represents 2, and so on. We iterate through the string from left to right, calculating the column number by multiplying the current result by 26 and adding the value of the current character.

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
            // Calculate the value of the current character ('A' - 'A' + 1 = 1, 'B' - 'A' + 1 = 2, etc.)
            int value = c - 'A' + 1;
            // Multiply the current result by 26 and add the value of the current character
            result = result * 26 + value;
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
- The problem can be solved by treating the Excel column title as a base-26 number system.
- We iterate through the string from left to right, calculating the column number by multiplying the current result by 26 and adding the value of the current character.
- The time complexity is O(n) where n is the length of the input string, and the space complexity is O(1) as we only use a constant amount of space.