# Excel Sheet Column Number

## Problem Statement
The problem requires converting an Excel sheet column title to its corresponding column number. The column title is a string consisting of uppercase letters, where 'A' represents the first column, 'B' represents the second column, and so on. The task is to write a function that takes a string `s` as input and returns the corresponding column number. For example, "A" corresponds to 1, "B" corresponds to 2, "Z" corresponds to 26, "AA" corresponds to 27, and "AZ" corresponds to 52.

## Approach
The approach is to iterate over the input string from left to right, treating each character as a digit in a base-26 number system. The value of each digit is determined by its position in the alphabet (A=1, B=2, ..., Z=26). The column number is calculated by multiplying the current result by 26 and adding the value of the current digit.

## Complexity
- Time: O(n), where n is the length of the input string
- Space: O(1), as only a constant amount of space is used

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
- The problem can be solved by treating the input string as a base-26 number
- The value of each digit is determined by its position in the alphabet
- The time complexity is linear with respect to the length of the input string