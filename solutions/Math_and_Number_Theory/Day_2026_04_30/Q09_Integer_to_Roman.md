# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000). The goal is to write a function that takes an integer as input and returns its Roman numeral equivalent. For example, the integer 4 is represented as IV, and 9 is represented as IX.

## Approach
The approach involves using a greedy algorithm to construct the Roman numeral representation. We start with the largest possible Roman numeral and subtract it from the number as many times as possible, then move to the next largest numeral, and so on. This process continues until the number becomes 0.

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
- Use a greedy approach to construct the Roman numeral representation.
- Utilize an array of values and corresponding Roman numerals to simplify the conversion process.
- Iterate through the array and subtract the largest possible value from the number, appending the corresponding Roman numeral to the result.