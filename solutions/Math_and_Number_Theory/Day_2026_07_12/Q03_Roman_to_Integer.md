# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires us to write a function that takes a string of Roman numerals as input and returns the integer equivalent. The input string will only contain the symbols I, V, X, L, C, D and M. The function should handle cases where the input string is empty or contains invalid Roman numerals. For example, the Roman numeral "III" represents the integer 3, "IV" represents 4, and "IX" represents 9.

## Approach
The approach is to iterate over the input string and add the value of each Roman numeral to a running total. If the current numeral is less than the next one, we subtract its value from the total instead of adding it. This is because in Roman numerals, a smaller numeral placed before a larger one means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of Roman numerals
    unordered_map<char, int> romanValues = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int total = 0;
    // Iterate over the input string
    for (int i = 0; i < s.length(); i++) {
        // If the current numeral is less than the next one, subtract its value
        if (i < s.length() - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {
            total -= romanValues[s[i]];
        } else {
            // Otherwise, add its value
            total += romanValues[s[i]];
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
- The key to solving this problem is to understand the rules of Roman numerals and how to handle cases where a smaller numeral appears before a larger one.
- Using a map to store the values of Roman numerals makes the code more efficient and easier to read.
- The time complexity of the solution is O(n), where n is the length of the input string, because we only need to iterate over the string once.