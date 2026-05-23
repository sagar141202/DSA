# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer can range from 1 to 3999. The Roman numerals use seven distinct symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The constraints are that the input integer should be between 1 and 3999, and the output should be a string representing the Roman numeral equivalent of the input integer. For example, the integer 4 is represented as IV, 9 as IX, 13 as XIII, 44 as XLIV, and 1000 as M.

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation by iterating over the decimal values of the Roman numerals in descending order and appending the corresponding Roman numeral to the result as many times as possible without exceeding the input integer.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string result = "";
        
        for (int i = 0; i < 13; i++) {
            while (num >= values[i]) {
                result += symbols[i];
                num -= values[i];
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: 3
Output: III
Input: 4
Output: IV
Input: 9
Output: IX
Input: 13
Output: XIII
Input: 44
Output: XLIV
Input: 1000
Output: M
```

## Key Takeaways
- Use a greedy approach to construct the Roman numeral representation.
- Iterate over the decimal values of the Roman numerals in descending order.
- Append the corresponding Roman numeral to the result as many times as possible without exceeding the input integer.