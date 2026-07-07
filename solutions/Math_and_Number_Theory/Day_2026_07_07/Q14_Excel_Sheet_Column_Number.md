# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The column title can contain multiple characters, and the column number can exceed the maximum limit of a 32-bit integer. For example, the column title "A" corresponds to the column number 1, "B" corresponds to 2, "Z" corresponds to 26, "AA" corresponds to 27, and "AZ" corresponds to 52.

## Approach
The algorithm uses the concept of base-26 numbers, where each character in the string represents a digit in the base-26 system. We iterate through the string from left to right, calculate the value of each character, and add it to the total column number.

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
            // add the value to the total column number
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
- The problem can be solved using the concept of base-26 numbers.
- We need to iterate through the string from left to right to calculate the column number.
- The time complexity is linear, and the space complexity is constant.