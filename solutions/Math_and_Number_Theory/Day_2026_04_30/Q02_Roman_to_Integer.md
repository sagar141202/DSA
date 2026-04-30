# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Given a roman numeral, convert it to an integer. The integer value of a roman numeral is calculated as follows: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. If a smaller numeral appears before a larger one, subtract the smaller numeral's value; otherwise, add it. For example, IV = 4 (5 - 1), IX = 9 (10 - 1), and XL = 40 (50 - 10). The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will be between 1 and 15 characters long.

## Approach
We can solve this problem by iterating over the input string, adding the value of each numeral to a running total, and subtracting the value if a smaller numeral appears before a larger one. We will use a map to store the values of the roman numerals.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // map to store the values of roman numerals
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
    for (int i = 0; i < s.length(); i++) {
        // if current numeral is smaller than the next one, subtract its value
        if (i < s.length() - 1 && roman[s[i]] < roman[s[i + 1]]) {
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
- Iterate over the input string, adding or subtracting the value of each numeral based on its position.
- The time complexity is O(n), where n is the length of the input string, because we make a single pass over the string.