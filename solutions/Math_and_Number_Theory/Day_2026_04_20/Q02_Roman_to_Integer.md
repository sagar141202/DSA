# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires us to convert a Roman numeral to an integer. For example, III is 3, IV is 4, IX is 9, LVIII is 58, MCMXCIV is 1994. The input will be a string containing only the characters I, V, X, L, C, D and M. The string will be between 1 and 15 characters long. The function should return the integer equivalent of the Roman numeral.

## Approach
The approach is to iterate over the string from left to right and add the value of the current numeral to the total if it is greater than or equal to the next numeral. If the current numeral is less than the next one, we subtract its value from the total. This way, we correctly handle cases like IV and IX.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of Roman numerals
    unordered_map<char, int> roman = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int total = 0;
    // Iterate over the string
    for (int i = 0; i < s.length(); i++) {
        // If the current numeral is less than the next one, subtract its value
        if (i < s.length() - 1 && roman[s[i]] < roman[s[i + 1]]) {
            total -= roman[s[i]];
        } else {
            // Otherwise, add its value
            total += roman[s[i]];
        }
    }
    return total;
}
```

## Test Cases
```
Input: "III"
Output: 3
Input: "IV"
Output: 4
Input: "IX"
Output: 9
Input: "LVIII"
Output: 58
Input: "MCMXCIV"
Output: 1994
```

## Key Takeaways
- Use a map to store the values of Roman numerals for easy lookup.
- Iterate over the string and compare each numeral with the next one to determine whether to add or subtract its value.
- Handle edge cases like IV and IX correctly by checking if the current numeral is less than the next one.