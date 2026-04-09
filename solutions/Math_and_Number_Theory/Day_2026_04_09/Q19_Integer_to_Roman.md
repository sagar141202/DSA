# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals use seven distinct symbols: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000). The solution should handle all possible integers within the given range and return the correct Roman numeral representation. For example, the integer 4 is represented as IV, and the integer 9 is represented as IX.

## Approach
The solution uses a greedy approach, iterating through the Roman numerals in descending order and subtracting the largest possible numeral value from the integer until it reaches 0. This approach ensures the most efficient and accurate conversion.

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
        vector<string> romanLiterals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string result = "";
        for (int i = 0; i < values.size(); i++) {
            while (num >= values[i]) {
                result += romanLiterals[i];
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
- The greedy approach is suitable for this problem, as it ensures the most efficient conversion by using the largest possible Roman numeral values first.
- The solution uses two vectors, one for the integer values and one for the corresponding Roman numerals, to simplify the conversion process.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.