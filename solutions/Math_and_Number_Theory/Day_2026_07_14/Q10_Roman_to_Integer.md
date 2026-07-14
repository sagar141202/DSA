# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The task is to convert a Roman numeral to an integer. The input will be a string containing only the characters I, V, X, L, C, D and M. The string will be between 1 and 15 characters long. For example, the Roman numeral "III" represents the integer 3, and "IV" represents 4. The Roman numeral "MMXXI" represents the integer 2021.

## Approach
We can solve this problem by iterating over the input string and adding the value of each numeral to a running total. If the current numeral is less than the next one, we subtract its value instead of adding it. This is because in Roman numerals, a smaller numeral placed before a larger one means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Map to store the values of Roman numerals
    unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    
    int total = 0;
    for (int i = 0; i < s.size(); i++) {
        // If the current numeral is less than the next one, subtract its value
        if (i + 1 < s.size() && roman[s[i]] < roman[s[i + 1]]) {
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
Input: "MMXXI"
Output: 2021
```

## Key Takeaways
- Use a map to store the values of Roman numerals for easy lookup.
- Iterate over the input string and add or subtract the value of each numeral based on whether it's less than the next one.
- The time complexity is O(n), where n is the length of the input string, because we make a single pass over the string.