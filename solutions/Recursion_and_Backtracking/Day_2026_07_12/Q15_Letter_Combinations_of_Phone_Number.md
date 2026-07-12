# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
- 2: 'a', 'b', 'c'
- 3: 'd', 'e', 'f'
- 4: 'g', 'h', 'i'
- 5: 'j', 'k', 'l'
- 6: 'm', 'n', 'o'
- 7: 'p', 'q', 'r', 's'
- 8: 't', 'u', 'v'
- 9: 'w', 'x', 'y', 'z'
Each digit can only be used once, and the order of the letters matters. For example, "23" can be represented as ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We can solve this problem using recursion and backtracking by iterating over each digit in the input string, and for each digit, trying all possible letters that it can represent. We then recursively call the function with the remaining digits and the current combination of letters.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, as in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursive call stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) return result;
        
        // Mapping of digits to letters
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        // Recursive function to generate combinations
        function<void(int, string)> backtrack = [&](int index, string current) {
            if (index == digits.size()) {
                result.push_back(current);
                return;
            }
            
            // Try all possible letters for the current digit
            for (char c : phone[digits[index] - '0']) {
                backtrack(index + 1, current + c);
            }
        };
        
        backtrack(0, "");
        return result;
    }
};
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters for a given phone number.
- Use a mapping of digits to letters to try all possible letters for each digit.
- The time complexity is exponential in the number of digits, as in the worst case, each digit can have 4 possible letters.