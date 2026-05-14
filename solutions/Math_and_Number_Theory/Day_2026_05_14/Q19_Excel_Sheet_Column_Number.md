# Excel Sheet Column Number

## Problem Statement
Given a string `s` which represents a column title in an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents 1, `B` represents 2, and so on. The title can contain multiple characters, and the column number is calculated based on the base-26 number system. For example, `AB` represents `(1 * 26) + 2 = 28`, and `ZY` represents `(26 * 26) + 26 = 702`.

## Approach
The solution involves iterating over the input string from left to right, calculating the corresponding numerical value of each character, and adding it to the total column number based on its position. The algorithm uses the base-26 number system to calculate the column number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (char c : s) {
            // Calculate the corresponding numerical value of the character
            // and add it to the total column number based on its position
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: "A"
Output: 1
Input: "AB"
Output: 28
Input: "ZY"
Output: 701
```

## Key Takeaways
- The problem can be solved using a simple iterative approach based on the base-26 number system.
- The time complexity is linear, and the space complexity is constant, making the solution efficient for large inputs.
- The solution involves calculating the corresponding numerical value of each character and adding it to the total column number based on its position.