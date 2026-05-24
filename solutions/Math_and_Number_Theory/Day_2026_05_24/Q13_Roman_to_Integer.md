# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral string to an integer. The input string will be between 1 and 15 characters long, containing only the above-mentioned symbols. The Roman numeral is guaranteed to be valid.

## Approach
The solution involves iterating over the input string, adding the value of each symbol to a running total, and subtracting the value of a symbol if it appears before a larger symbol. This approach works because in Roman numerals, a smaller symbol placed before a larger symbol means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
        for (int i = 0; i < s.length(); i++) {
            // If the current symbol is not the last symbol and its value is less than the next symbol's value
            if (i < s.length() - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {
                // Subtract the value of the current symbol from the total
                total -= romanValues[s[i]];
            } else {
                // Add the value of the current symbol to the total
                total += romanValues[s[i]];
            }
        }
        return total;
    }
};
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
- The key to solving this problem is understanding the rules of Roman numerals, particularly the subtraction rule.
- Using an unordered map to store the values of Roman numerals makes the code more readable and efficient.
- The solution has a time complexity of O(n), where n is the length of the input string, because it involves a single pass over the string.