# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which correspond to the values 1, 5, 10, 50, 100, 500, and 1000 respectively. For example, the integer 4 is represented as IV, 9 as IX, and 58 as LVIII.

## Approach
The approach involves using a greedy algorithm to construct the Roman numeral representation. We start with the largest possible Roman numeral and subtract its value from the integer until we cannot subtract anymore, then move to the next smaller numeral.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <string>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            num -= values[i];
            result += symbols[i];
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
Input: 58
Output: LVIII
Input: 1994
Output: MCMXCIV
```

## Key Takeaways
- Use a greedy algorithm to construct the Roman numeral representation.
- Start with the largest possible Roman numeral and subtract its value from the integer until we cannot subtract anymore.
- Use an array to store the values and corresponding symbols of the Roman numerals.