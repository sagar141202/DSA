# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the 1st column, `B` represents the 2nd column, and so on. The same pattern applies when the column number exceeds 26, with `AA` representing the 27th column, `AB` representing the 28th column, and so on. The input string `s` will not be empty and will only contain uppercase letters.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number, where each digit is represented by a letter from `A` to `Z`. We can then convert this base-26 number to a decimal number, which represents the column number. The algorithm involves iterating over the input string from left to right, calculating the value of each digit, and adding it to the total column number.

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
            // Calculate the value of the current digit and add it to the result
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
- The problem can be solved by treating the Excel column title as a base-26 number.
- The algorithm involves iterating over the input string from left to right and calculating the value of each digit.
- The time complexity of the solution is O(n), where n is the length of the input string.