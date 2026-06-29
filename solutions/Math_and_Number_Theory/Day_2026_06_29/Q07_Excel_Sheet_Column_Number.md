# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet as it appears in an Excel formula bar, return its corresponding column number. The column title is in the range `[A, ZZ]`, where `A` represents column 1, `B` represents column 2, ..., `Z` represents column 26, `AA` represents column 27, `AB` represents column 28, and so on. For example, the column title `"A"` corresponds to column number `1`, `"B"` corresponds to `2`, `"Z"` corresponds to `26`, `"AA"` corresponds to `27`, and `"AZ"` corresponds to `52`.

## Approach
The problem can be solved using the concept of base-26 numbers, where each digit in the base-26 number corresponds to a letter from `A` to `Z`. We iterate over the string from left to right, calculate the value of each character, and add it to the total value. The value of each character is calculated as `(character - 'A' + 1) * 26^(length - i - 1)`, where `i` is the current index and `length` is the length of the string.

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
        for (int i = 0; i < s.length(); i++) {
            // calculate the value of the current character
            int value = (s[i] - 'A' + 1) * pow(26, s.length() - i - 1);
            // add the value to the total result
            result += value;
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
- The problem can be solved using the concept of base-26 numbers.
- The value of each character is calculated based on its position in the string.
- The time complexity is O(n), where n is the length of the input string.