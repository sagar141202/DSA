# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which correspond to the decimal values 1, 5, 10, 50, 100, 500, and 1000, respectively. The constraints are that the input integer is between 1 and 3999, and the output should be a string representing the Roman numeral equivalent of the input integer. For example, the integer 4 is represented as IV, and the integer 9 is represented as IX.

## Approach
The algorithm involves using a greedy approach to subtract the largest possible Roman numeral values from the input integer until it becomes 0. The intuition is to use the largest possible Roman numerals first to minimize the number of symbols required to represent the integer. This approach ensures that the resulting Roman numeral is valid and follows the standard rules of Roman numeral representation.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

int main() {
    int num = 2024;
    cout << intToRoman(num) << endl;
    return 0;
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
- The greedy approach is used to subtract the largest possible Roman numeral values from the input integer.
- The algorithm uses two arrays, one for the decimal values and one for the corresponding Roman numeral symbols.
- The time complexity is O(1) because the number of iterations is constant, and the space complexity is O(1) because the space used does not grow with the input size.