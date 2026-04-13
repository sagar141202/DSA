# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is given as input and should be within the range of 1 to 3999. The Roman numerals use seven letters: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The goal is to write a function that takes an integer as input and returns its Roman numeral equivalent. For example, the integer 4 should be converted to "IV", 9 to "IX", 13 to "XIII", 44 to "XLIV", and 1000 to "M".

## Approach
The approach involves using a greedy algorithm to construct the Roman numeral representation by subtracting the largest possible Roman numeral values from the input integer. This is done by using an array of Roman numerals and their corresponding integer values. The algorithm iterates through the array from largest to smallest, appending the Roman numeral to the result and subtracting its value from the input integer as long as possible.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            result += roman[i];
            num -= values[i];
        }
    }
    return result;
}
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
- The greedy algorithm is used to construct the Roman numeral representation.
- The array of Roman numerals and their corresponding integer values is used to iterate through the possible values from largest to smallest.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.