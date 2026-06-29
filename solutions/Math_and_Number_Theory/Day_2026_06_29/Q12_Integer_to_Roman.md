# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which have values of 1, 5, 10, 50, 100, 500, and 1000 respectively. The task is to write a function that takes an integer as input and returns its Roman numeral equivalent. For example, the integer 3 is represented as III, 4 is represented as IV, 9 is represented as IX, and 58 is represented as LVIII.

## Approach
The algorithm involves using a greedy approach to construct the Roman numeral representation by iterating over the integer value from largest to smallest and appending the corresponding Roman numeral symbols. This is achieved by using a list of tuples containing the decimal values and their corresponding Roman numerals.

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
        vector<pair<int, string>> values = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};
        string result = "";
        
        for (auto& value : values) {
            while (num >= value.first) {
                num -= value.first;
                result += value.second;
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
Input: 58
Output: LVIII
Input: 1994
Output: MCMXCIV
```

## Key Takeaways
- Use a greedy approach to construct the Roman numeral representation.
- Utilize a list of tuples containing decimal values and their corresponding Roman numerals.
- Iterate over the integer value from largest to smallest and append the corresponding Roman numeral symbols.