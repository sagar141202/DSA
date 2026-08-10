# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer can range from 1 to 3999. Roman numerals use seven distinct symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The Roman numeral system is based on a set of rules where each symbol can be repeated up to three times, and a smaller symbol placed before a larger one means subtraction. For example, the number 4 is represented as IV (5 - 1), and the number 9 is represented as IX (10 - 1). The goal is to write a function that takes an integer as input and returns its Roman numeral representation as a string.

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation by iterating over the decimal values of the Roman numerals in descending order. It subtracts the largest possible Roman numeral value from the number and appends the corresponding symbol to the result string, repeating this process until the number becomes 0.

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
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string result = "";
        
        for (int i = 0; i < values.size(); i++) {
            while (num >= values[i]) {
                num -= values[i];
                result += symbols[i];
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
- The greedy approach is used to construct the Roman numeral representation.
- The algorithm iterates over the decimal values of the Roman numerals in descending order.
- The time complexity is O(1) because the number of iterations is constant, and the space complexity is O(1) because the space used does not grow with the size of the input.