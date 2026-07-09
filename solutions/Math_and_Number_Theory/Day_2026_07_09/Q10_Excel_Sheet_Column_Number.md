# Excel Sheet Column Number

## Problem Statement
Given a string `columnTitle` representing the column title as it appears in an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The column title can contain multiple characters, for example, `AA` represents the 27th column, `AB` represents the 28th column, and `ZZ` represents the 702nd column. The input string `columnTitle` will not be empty and will only contain uppercase letters.

## Approach
The algorithm uses the concept of base-26 numbers, where each character in the string represents a digit in base-26. The value of each digit is calculated by subtracting the ASCII value of 'A' from the ASCII value of the character and adding 1. The column number is then calculated by summing up the values of all digits multiplied by their respective place values.

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
            // calculate the value of the current digit
            int digit = c - 'A' + 1;
            // update the result by shifting the current digits to the left and adding the new digit
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
Input: "ZZ"
Output: 702
```

## Key Takeaways
- The problem can be solved using the concept of base-26 numbers.
- The value of each digit is calculated by subtracting the ASCII value of 'A' from the ASCII value of the character and adding 1.
- The column number is calculated by summing up the values of all digits multiplied by their respective place values.