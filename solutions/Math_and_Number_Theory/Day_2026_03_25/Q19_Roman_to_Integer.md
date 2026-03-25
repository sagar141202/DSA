# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The integer value of a roman numeral is determined by adding the values of its symbols, with the exception that if a smaller symbol appears before a larger one, its value is subtracted from the total. For example, IV represents 4 (5 - 1) and IX represents 9 (10 - 1). Given a roman numeral as a string, convert it to an integer. The input string will be between 1 and 15 characters long, and will only contain the characters I, V, X, L, C, D and M. For example, input "III" should return 3, input "IV" should return 4, and input "IX" should return 9.

## Approach
The approach is to iterate over the string from left to right, adding the value of each symbol to a running total. If a smaller symbol appears before a larger one, we subtract the value of the smaller symbol from the total instead of adding it. We use a map to store the values of the roman numerals.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of roman numerals
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
    for (int i = 0; i < s.size(); i++) {
        // If the current symbol is smaller than the next one, subtract its value
        if (i + 1 < s.size() && roman[s[i]] < roman[s[i + 1]]) {
            total -= roman[s[i]];
        } else {
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
- Use a map to store the values of roman numerals for easy lookup.
- Iterate over the string from left to right, adding or subtracting the value of each symbol based on whether it is smaller than the next symbol.
- The time complexity is O(n), where n is the length of the input string, because we make a single pass over the string. The space complexity is O(1) because we use a fixed amount of space to store the map of roman numerals.