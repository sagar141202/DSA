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
A number can have multiple combinations, for example, the number "23" can be represented as "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf". The input will not contain 0 or 1.

## Approach
We will use a recursive backtracking approach to generate all possible combinations. We will iterate over each digit in the input string, and for each digit, we will iterate over its corresponding letters. We will then recursively call the function with the remaining digits and the current combination of letters.

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
        
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, vector<string>& phone, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        string letters = phone[digits[index] - '0'];
        for (char letter : letters) {
            backtrack(result, phone, digits, index + 1, current + letter);
        }
    }
};

```

## Test Cases
```
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Key Takeaways
- The problem can be solved using a recursive backtracking approach.
- The time complexity is O(4^n) due to the worst-case scenario where each digit has 4 possible letters.
- The space complexity is O(n) due to the recursive call stack.