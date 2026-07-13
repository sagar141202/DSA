# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The same letter can be used multiple times, and the title can be a combination of uppercase letters. For example, `AB` corresponds to the column number `28` because `A` is the first column and `B` is the second column. The function should return the column number for a given Excel sheet column title.

## Approach
The algorithm uses the concept of base-26 numbering, where each letter in the title represents a digit in base-26. The approach involves iterating over the title from left to right, calculating the value of each digit, and summing them up to get the final column number.

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
            // calculate the value of the current digit
            int digit = c - 'A' + 1;
            // update the result
            result = result * 26 + digit;
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
- The problem can be solved using base-26 numbering.
- Each character in the string represents a digit in base-26, with 'A' being 1, 'B' being 2, and so on.
- The time complexity is linear because we only iterate over the string once.