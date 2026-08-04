# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the format of letters from A to Z, where A represents 1, B represents 2, ..., Z represents 26, AA represents 27, and so on. The constraint is that 1 <= s.length <= 2147483647 and s consists only of uppercase English letters.

## Approach
The algorithm is based on the concept of base-26 numbers, where each digit represents a letter from A to Z. We can iterate over the string from left to right, calculate the value of each digit, and add it to the total sum after multiplying it by the corresponding power of 26.

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
            int digitValue = c - 'A' + 1;
            // add the value to the total sum after multiplying by the corresponding power of 26
            result = result * 26 + digitValue;
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
- We can calculate the value of each digit by subtracting the ASCII value of 'A' and adding 1.
- The time complexity is linear, and the space complexity is constant.