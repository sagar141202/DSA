# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Each letter can only be used once in each combination, and the order of the combinations does not matter. The input will not contain any space, and will not contain any non-digit characters. The input will not be empty, and will not contain any digits outside of 2-9. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
The problem can be solved using recursion and backtracking. We will create a mapping of digits to their corresponding letters, and then use a recursive function to generate all possible combinations. The function will take the current combination and the remaining digits as parameters, and will add each possible letter to the combination and recursively call itself with the updated combination and the remaining digits.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, since each digit can have up to 4 possible letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        
        // Mapping of digits to their corresponding letters
        vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        vector<string> result;
        string current;
        
        // Recursive function to generate all possible combinations
        function<void(int)> backtrack = [&](int index) {
            if (index == digits.size()) {
                result.push_back(current);
                return;
            }
            
            // Get the possible letters for the current digit
            string letters = mapping[digits[index] - '0'];
            
            // Add each possible letter to the current combination and recursively call the function
            for (char letter : letters) {
                current.push_back(letter);
                backtrack(index + 1);
                current.pop_back();
            }
        };
        
        backtrack(0);
        
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
- Use recursion and backtracking to generate all possible combinations.
- Create a mapping of digits to their corresponding letters to simplify the solution.
- Use a recursive function to add each possible letter to the current combination and generate all possible combinations.