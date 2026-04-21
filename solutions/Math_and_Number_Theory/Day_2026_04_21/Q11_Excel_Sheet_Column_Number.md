# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing a column title of an Excel sheet, return its corresponding column number. The column title is in the format of `A`, `B`, `C`, ..., `Z`, `AA`, `AB`, ..., `AZ`, `BA`, `BB`, ..., `ZZ`, `AAA`, and so on. The input string `s` will only contain uppercase letters, and its length will be in the range `[1, 2147483647]`. For example, `A` corresponds to `1`, `B` corresponds to `2`, `Z` corresponds to `26`, `AA` corresponds to `27`, and `AZ` corresponds to `52`.

## Approach
The problem can be solved by treating the column title as a base-26 number, where `A` represents `1`, `B` represents `2`, and so on. We can iterate over the string from left to right, calculate the value of each character, and add it to the total column number. The value of each character is calculated by multiplying the previous total by `26` and adding the value of the current character.

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
            // multiply the previous total by 26 and add the value of the current character
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
- The problem can be solved by treating the column title as a base-26 number.
- The value of each character is calculated by subtracting the ASCII value of 'A' and adding 1.
- The time complexity is O(n), where n is the length of the input string.