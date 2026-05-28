# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The title can contain multiple characters, with `Z` representing 26, `AA` representing 27, `AB` representing 28, and so on. For example, given `s = "A"`, return `1`, given `s = "AB"`, return `28`, and given `s = "ZY"`, return `701`.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number, where each character represents a digit in this base-26 system. We iterate over the string from left to right, calculate the value of each character, and add it to the total value. The value of each character is calculated by multiplying its position value by 26 raised to the power of its position from the right.

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
            // Calculate the value of the current character
            int value = c - 'A' + 1;
            // Add the value to the result, taking into account the base-26 system
            result = result * 26 + value;
        }
        return result;
    }
};
```

## Test Cases
```
Input: s = "A"
Output: 1
Input: s = "AB"
Output: 28
Input: s = "ZY"
Output: 701
```

## Key Takeaways
- The problem can be solved by treating the Excel column title as a base-26 number.
- The value of each character is calculated by multiplying its position value by 26 raised to the power of its position from the right.
- The time complexity of the solution is O(n), where n is the length of the input string.