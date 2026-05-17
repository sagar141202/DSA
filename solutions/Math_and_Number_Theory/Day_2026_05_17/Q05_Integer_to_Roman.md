# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which correspond to the values 1, 5, 10, 50, 100, 500, and 1000, respectively. The Roman numeral system is based on a set of rules, where a smaller numeral placed before a larger one means subtraction, and the same or smaller numeral placed after a larger one means addition. For example, the integer 4 is represented as IV (5 - 1), and the integer 9 is represented as IX (10 - 1).

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation. It starts with the largest possible Roman numerals and subtracts the corresponding value from the integer until it becomes 0. This process is repeated for each Roman numeral symbol, from largest to smallest.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    // Define the Roman numerals and their corresponding values
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    string result = "";
    // Iterate over the Roman numerals and subtract the corresponding value from the integer
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            result += symbols[i];
            num -= values[i];
        }
    }

    return result;
}

int main() {
    int num = 1234;
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
Input: 13
Output: XIII
Input: 44
Output: XLIV
Input: 1000
Output: M
```

## Key Takeaways
- The greedy approach is used to construct the Roman numeral representation.
- The algorithm iterates over the Roman numerals in descending order of their values.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.