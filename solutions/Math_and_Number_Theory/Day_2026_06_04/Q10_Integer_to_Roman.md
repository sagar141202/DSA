# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. Roman numerals use seven distinct symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The Roman numeral representation of a number is obtained by combining these symbols in a specific way. For example, the number 4 is represented as IV, 9 as IX, 13 as XIII, and 44 as XLIV. The goal is to write a function that takes an integer as input and returns its Roman numeral representation as a string.

## Approach
The solution involves using a greedy approach to construct the Roman numeral representation by iteratively subtracting the largest possible Roman numeral value from the input number. This is done by maintaining a list of Roman numeral values and their corresponding symbols, and then iterating over this list to construct the representation.

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
        // Define the Roman numeral values and symbols
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        // Initialize the result string
        string result = "";
        
        // Iterate over the Roman numeral values and symbols
        for (int i = 0; i < 13; i++) {
            // Subtract the current Roman numeral value from the input number as many times as possible
            while (num >= values[i]) {
                // Append the corresponding symbol to the result string
                result += symbols[i];
                // Subtract the current Roman numeral value from the input number
                num -= values[i];
            }
        }
        
        // Return the Roman numeral representation
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
- The greedy approach is used to construct the Roman numeral representation by iteratively subtracting the largest possible Roman numeral value from the input number.
- A list of Roman numeral values and their corresponding symbols is maintained to facilitate the construction of the representation.
- The solution has a time complexity of O(1) because the number of iterations is constant and does not depend on the input size.