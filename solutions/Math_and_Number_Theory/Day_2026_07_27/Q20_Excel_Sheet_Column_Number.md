# Excel Sheet Column Number

## Problem Statement
Given a string `s` which represents the column title of an Excel sheet, return its corresponding column number. The title is a string of uppercase letters, and the column number is calculated as follows: 'A' corresponds to 1, 'B' corresponds to 2, ..., 'Z' corresponds to 26, 'AA' corresponds to 27, 'AB' corresponds to 28, and so on. The input string `s` is guaranteed to be a valid Excel column title.

## Approach
The algorithm involves converting the Excel column title to a base-26 number system, where each character represents a digit in the base-26 system. We iterate over the input string from left to right, calculate the value of each character, and add it to the total column number.

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
            // calculate the value of the current character and add it to the result
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
- The Excel column title can be viewed as a base-26 number system.
- Each character in the title represents a digit in the base-26 system, with 'A' corresponding to 1 and 'Z' corresponding to 26.
- The column number can be calculated by iterating over the input string and adding the value of each character to the total result.