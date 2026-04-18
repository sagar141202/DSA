# Excel Sheet Column Number

## Problem Statement
Given a string `s` which represents the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A = 1`, `B = 2`, ..., `Z = 26`, and `AA = 27`, `AB = 28`, ..., `AZ = 52`, and so on. For example, given `s = "A"`, return `1`. Given `s = "AB"`, return `28`. Given `s = "ZY"`, return `701`.

## Approach
The algorithm works by treating the Excel column title as a base-26 number, where `A` represents 1, `B` represents 2, and so on. We iterate over the string from left to right, calculating the value of each digit based on its position and adding it to the total.

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
            // Calculate the value of the current digit
            int digit = c - 'A' + 1;
            // Add the value of the current digit to the result
            result = result * 26 + digit;
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
- We can calculate the value of each digit based on its position in the string.
- The time complexity is O(n), where n is the length of the input string, because we iterate over the string once.