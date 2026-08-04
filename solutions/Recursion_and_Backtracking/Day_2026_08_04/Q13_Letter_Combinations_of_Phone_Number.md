# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
2 -> 'a', 'b', 'c'
3 -> 'd', 'e', 'f'
4 -> 'g', 'h', 'i'
5 -> 'j', 'k', 'l'
6 -> 'm', 'n', 'o'
7 -> 'p', 'q', 'r', 's'
8 -> 't', 'u', 'v'
9 -> 'w', 'x', 'y', 'z'
A number can be represented as a string of letters, and each digit can map to multiple letters. For example, "23" can be represented as "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf". 

## Approach
The problem can be solved using recursion and backtracking. We can create a recursive function that tries all possible letters for each digit and adds them to the current combination. The function will backtrack when it has tried all possible letters for a digit.

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Mapping of digits to letters
        vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        vector<string> result;
        if (digits.empty()) {
            return result;
        }
        
        // Recursive function to generate all combinations
        function<void(int, string)> backtrack = [&](int index, string current) {
            if (index == digits.size()) {
                result.push_back(current);
                return;
            }
            
            string letters = mapping[digits[index] - '0'];
            for (char letter : letters) {
                backtrack(index + 1, current + letter);
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
- Use recursion and backtracking to generate all possible combinations.
- Create a mapping of digits to letters to simplify the code.
- Use a recursive function to try all possible letters for each digit and add them to the current combination.