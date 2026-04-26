# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, AYZ]`. For example, `A` corresponds to `1`, `B` corresponds to `2`, ..., `Z` corresponds to `26`, `AA` corresponds to `27`, and so on. The input string `s` will always be a valid column title.

## Approach
The algorithm involves treating the Excel column title as a base-26 number, where each character represents a digit in this base-26 system. We iterate through the string from left to right, calculate the value of each character, and add it to the total column number.

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
- The problem can be solved by treating the Excel column title as a base-26 number.
- We iterate through the string from left to right and calculate the value of each character.
- The time complexity is O(n), where n is the length of the input string, and the space complexity is O(1) as we only use a constant amount of space.