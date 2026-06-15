# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer can range from 1 to 3999. The Roman numeral system uses seven letters: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The constraints are that the input integer should be between 1 and 3999, and the output should be a string representing the Roman numeral equivalent of the input integer. For example, the integer 4 should be converted to "IV", and the integer 9 should be converted to "IX".

## Approach
The approach to solve this problem involves using a greedy algorithm to construct the Roman numeral representation. We will use an array of integers and their corresponding Roman numerals to iterate through the input integer and append the largest possible Roman numeral to the result.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string romans[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            result += romans[i];
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
- The greedy algorithm is used to construct the Roman numeral representation by iterating through the input integer and appending the largest possible Roman numeral to the result.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.
- The space complexity is O(1) because the space required does not change with the size of the input integer.