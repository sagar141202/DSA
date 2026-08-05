# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires converting a Roman numeral to an integer. The input will be a string containing only the characters I, V, X, L, C, D and M. The string will be between 1 and 15 characters long. For example, the Roman numeral "III" represents the integer 3, and "IV" represents 4. The Roman numeral "IX" represents 9, and "LVIII" represents 58.

## Approach
The algorithm uses a hashmap to store the Roman numerals and their corresponding integer values. It then iterates over the input string, adding the value of each numeral to a running total. If the current numeral is less than the next one, it subtracts the value of the current numeral from the total instead of adding it.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    int total = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i + 1 < s.length() && roman[s[i]] < roman[s[i + 1]]) {
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
- Use a hashmap to store the Roman numerals and their corresponding integer values for efficient lookup.
- Iterate over the input string, considering each character and the next one to determine whether to add or subtract the value from the total.
- The solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1) since the size of the hashmap is constant.