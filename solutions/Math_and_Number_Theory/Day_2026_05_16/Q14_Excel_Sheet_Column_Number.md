# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the format of letters from A to Z, where A represents 1, B represents 2, ..., Z represents 26, AA represents 27, AB represents 28, and so on. The input string `s` will only contain uppercase letters, and its length will be between 1 and 10. For example, if `s` is "A", the output should be 1, if `s` is "B", the output should be 2, if `s` is "AA", the output should be 27, and if `s` is "AB", the output should be 28.

## Approach
The algorithm uses the concept of base-26 numbers, where each digit in the string represents a power of 26. We iterate through the string from left to right, calculating the value of each character and adding it to the total sum. The intuition is to treat the string as a base-26 number and convert it to decimal.

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
Input: "B"
Output: 2
Input: "AA"
Output: 27
Input: "AB"
Output: 28
```

## Key Takeaways
- The problem can be solved by treating the input string as a base-26 number and converting it to decimal.
- The time complexity is O(n), where n is the length of the input string, because we only need to iterate through the string once.
- The space complexity is O(1), because we only use a constant amount of space to store the result and the current character.