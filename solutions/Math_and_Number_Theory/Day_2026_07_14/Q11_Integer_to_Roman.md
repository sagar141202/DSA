# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals use seven symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The conversion should follow the standard Roman numeral rules, where a smaller number placed before a larger number means subtraction, and addition otherwise. For example, the integer 4 is represented as IV (5 - 1), and 9 is represented as IX (10 - 1).

## Approach
The algorithm involves looping through the integer value and subtracting the largest possible Roman numeral value at each step. This process continues until the integer value becomes 0. The corresponding Roman numeral symbols are appended to the result string at each step.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        // Define the Roman numeral symbols and their corresponding values
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        // Initialize an empty result string
        string result = "";
        
        // Loop through the integer value and append the corresponding Roman numeral symbols
        for (int i = 0; i < values.size(); i++) {
            while (num >= values[i]) {
                result += symbols[i];
                num -= values[i];
            }
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    cout << solution.intToRoman(3) << endl;  // Output: III
    cout << solution.intToRoman(4) << endl;  // Output: IV
    cout << solution.intToRoman(9) << endl;  // Output: IX
    cout << solution.intToRoman(13) << endl;  // Output: XIII
    cout << solution.intToRoman(44) << endl;  // Output: XLIV
    cout << solution.intToRoman(1000) << endl;  // Output: M
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
- The solution uses a greedy approach to subtract the largest possible Roman numeral value at each step.
- The time complexity is O(log n) due to the number of loops required to process the integer value.
- The space complexity is O(log n) due to the space required to store the result string.