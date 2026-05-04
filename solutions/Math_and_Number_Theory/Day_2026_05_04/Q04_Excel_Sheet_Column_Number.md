# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the format of `A`, `B`, `C`, ..., `Z`, `AA`, `AB`, ..., `AZ`, `BA`, `BB`, ..., `ZZ`, `AAA`, and so on. The column number starts from 1. For example, given `s = "A"`, return `1`. Given `s = "AB"`, return `28`. Given `s = "ZY"`, return `701`.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number system, where `A` represents 1, `B` represents 2, and so on. We can iterate through the string from left to right, calculate the value of each character, and add it to the total column number.

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
            // calculate the value of the current character
            int value = c - 'A' + 1;
            // add the value to the total column number
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
- The Excel column title can be treated as a base-26 number system.
- We can calculate the column number by iterating through the string from left to right and adding the value of each character to the total.
- The time complexity is O(n), where n is the length of the input string.