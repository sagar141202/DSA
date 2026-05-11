# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
2 -> 'a', 'b', 'c', 
3 -> 'd', 'e', 'f', 
4 -> 'g', 'h', 'i', 
5 -> 'j', 'k', 'l', 
6 -> 'm', 'n', 'o', 
7 -> 'p', 'q', 'r', 's', 
8 -> 't', 'u', 'v', 
9 -> 'w', 'x', 'y', 'z'. 
Note that 1 and 0 are not mapped. 
Example: Input: "23" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

## Approach
We will use recursion and backtracking to generate all possible combinations. The algorithm will iterate over each digit in the input string, and for each digit, it will iterate over all possible letters that the digit can represent. We will use a helper function to perform the recursion.

## Complexity
- Time: O(4^n) where n is the length of the input string, because in the worst case, each digit can represent 4 letters.
- Space: O(n) for the recursion stack.

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
Input: ""
Output: []
Input: "2"
Output: ["a","b","c"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations.
- Use a helper function to perform the recursion.
- The time complexity is O(4^n) in the worst case, where n is the length of the input string.