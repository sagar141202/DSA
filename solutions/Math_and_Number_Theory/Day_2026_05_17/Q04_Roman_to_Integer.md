# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem is to convert a Roman numeral to an integer. The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will be between 1 and 15 characters long. For example, the Roman numeral "III" represents the integer 3, and "IV" represents the integer 4. The Roman numeral "MMXXI" represents the integer 2021.

## Approach
The algorithm works by iterating over the input string from left to right, adding the value of each symbol to a running total. If the current symbol is less than the next symbol, we subtract its value from the total instead of adding it. This is because in Roman numerals, a smaller symbol placed before a larger symbol means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the integer values of Roman numerals
    unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    
    int total = 0;
    for (int i = 0; i < s.length(); i++) {
        // If the current symbol is less than the next symbol, subtract its value
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
Input: "MMXXI"
Output: 2021
```

## Key Takeaways
- Use a map to store the integer values of Roman numerals for efficient lookups.
- Iterate over the input string from left to right, considering the value of each symbol in relation to the next symbol.
- Handle the case where a smaller symbol appears before a larger symbol by subtracting its value from the total.