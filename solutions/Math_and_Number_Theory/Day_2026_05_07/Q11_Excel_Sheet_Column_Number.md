# Excel Sheet Column Number

## Problem Statement
Given a string `columnTitle` representing the column title as it appears in an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents 1, `B` represents 2, and so on. For example, `A` is 1, `B` is 2, `Z` is 26, `AA` is 27, and `AZ` is 52.

## Approach
The algorithm involves iterating over the input string from left to right, with each character contributing to the total column number based on its position and value. The intuition is to treat the column title as a base-26 number system.

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
            // Calculate the value of the current character
            int value = c - 'A' + 1;
            // Update the result by shifting the current value to the left (base-26) and adding the new value
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
- The time complexity is linear with respect to the length of the input string.
- The space complexity is constant, as only a fixed amount of space is used to store the result.