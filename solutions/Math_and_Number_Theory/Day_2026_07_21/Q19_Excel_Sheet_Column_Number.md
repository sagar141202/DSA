# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the format of "A", "B", "C", ..., "Z", "AA", "AB", ..., "AZ", "BA", "BB", ..., "ZZ", ... . The column number starts from 1. For example, given `s = "A"`, return `1`. Given `s = "AB"`, return `28`. Given `s = "ZY"`, return `701`.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number system, where 'A' represents 1, 'B' represents 2, and so on. We iterate through the string from left to right, calculate the value of each character, and add it to the total column number. The value of each character is calculated by multiplying the current value by 26 and adding the value of the current character.

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
            // Update the result
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
- The value of each character is calculated by multiplying the current value by 26 and adding the value of the current character.
- The solution has a time complexity of O(n), where n is the length of the input string.