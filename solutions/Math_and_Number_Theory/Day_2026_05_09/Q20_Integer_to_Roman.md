# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which correspond to the decimal values 1, 5, 10, 50, 100, 500, and 1000 respectively. The goal is to develop an algorithm that can efficiently convert any given integer within the specified range to its Roman numeral equivalent.

## Approach
The approach involves using a greedy algorithm to construct the Roman numeral representation by iteratively subtracting the largest possible Roman numeral value from the input integer. This process continues until the integer becomes 0. The algorithm utilizes an array of Roman numeral values and their corresponding symbols to simplify the conversion process.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    // Define the Roman numeral values and symbols
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    
    // Initialize an empty string to store the Roman numeral representation
    string roman = "";
    
    // Iterate over the Roman numeral values and symbols
    for (int i = 0; i < 13; i++) {
        // Subtract the current Roman numeral value from the input integer as many times as possible
        while (num >= values[i]) {
            // Append the corresponding Roman numeral symbol to the result string
            roman += symbols[i];
            // Subtract the current Roman numeral value from the input integer
            num -= values[i];
        }
    }
    
    // Return the resulting Roman numeral representation
    return roman;
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
Input: 13
Output: XIII
Input: 44
Output: XLIV
Input: 1000
Output: M
```

## Key Takeaways
- The greedy algorithm is used to construct the Roman numeral representation by iteratively subtracting the largest possible Roman numeral value from the input integer.
- The algorithm utilizes an array of Roman numeral values and their corresponding symbols to simplify the conversion process.
- The time complexity of the algorithm is O(log n) due to the iterative subtraction of Roman numeral values, where n is the input integer.