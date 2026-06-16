# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral to its corresponding integer value. The input is a string of Roman numerals, and the output is the integer value. For example, "III" is equal to 3, "IV" is equal to 4, and "IX" is equal to 9. The input string will only contain the characters I, V, X, L, C, D, and M.

## Approach
The approach to solve this problem is to iterate over the input string and add the value of each Roman numeral to a running total. If the current numeral is less than the next one, subtract its value from the total instead of adding it. This is because in Roman numerals, a smaller numeral placed before a larger one means subtraction.

## Complexity
- Time: O(n), where n is the length of the input string
- Space: O(1), as the space used does not grow with the size of the input

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of Roman numerals
    map<char, int> romanValues = {
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
        // If the current numeral is not the last one and its value is less than the next one
        if (i < s.length() - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {
            // Subtract the value of the current numeral from the total
            total -= romanValues[s[i]];
        } else {
            // Add the value of the current numeral to the total
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
- The key to solving this problem is to understand the rules of Roman numerals and how to handle subtraction.
- Using a map to store the values of Roman numerals makes the code more readable and easier to maintain.
- The time complexity is linear because we only need to iterate over the input string once.