# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is given in the range [1, 3999]. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which correspond to the decimal values 1, 5, 10, 50, 100, 500, and 1000 respectively. For example, the integer 4 is represented as IV, 9 as IX, 13 as XIII, 44 as XLIV, and 1000 as M.

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation by subtracting the largest possible Roman numeral value from the integer until it becomes 0. This is done by maintaining a list of Roman numeral values and their corresponding symbols, and then iterating over the list to construct the representation.

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
    int num = 1994;
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
- A list of Roman numeral values and their corresponding symbols is maintained to facilitate the construction process.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.