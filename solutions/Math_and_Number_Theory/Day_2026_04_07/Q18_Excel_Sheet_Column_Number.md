# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The title is a string of uppercase letters, and each letter represents a number (A = 1, B = 2, ..., Z = 26). The column number is calculated by treating the title as a base-26 number. For example, "A" corresponds to 1, "B" corresponds to 2, ..., "Z" corresponds to 26, "AA" corresponds to 27, and "AZ" corresponds to 52.

## Approach
The algorithm involves iterating over the input string from left to right, calculating the value of each character, and adding it to the total column number. The value of each character is calculated by multiplying the current total by 26 and adding the value of the current character.

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
            // update the result
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
- The problem can be solved by treating the Excel column title as a base-26 number.
- The time complexity is linear because we only need to iterate over the input string once.
- The space complexity is constant because we only use a fixed amount of space to store the result and other variables.