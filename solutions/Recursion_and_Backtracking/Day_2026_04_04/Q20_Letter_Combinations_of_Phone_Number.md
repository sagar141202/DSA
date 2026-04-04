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
Each digit can only be used once, and the order of the letters matters. For example, "23" could represent "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", or "cf".

## Approach
The problem can be solved using recursion and backtracking. We start with an empty string and try to append all possible letters for each digit. If we have tried all digits, we add the current string to the result.

## Complexity
- Time: O(4^n) where n is the length of the input string, because each digit can have at most 4 possible letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(string& digits, int start, string& path, vector<string>& result, unordered_map<char, string>& phone) {
    if (start == digits.size()) {
        result.push_back(path);
        return;
    }
    for (char c : phone[digits[start]]) {
        path.push_back(c);
        backtrack(digits, start + 1, path, result, phone);
        path.pop_back();
    }
}

vector<string> letterCombinations(string digits) {
    if (digits.empty()) return {};
    unordered_map<char, string> phone = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    vector<string> result;
    string path;
    backtrack(digits, 0, path, result, phone);
    return result;
}
```

## Test Cases
```
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require trying all possible combinations.
- Use an unordered_map to store the mapping of digits to letters for easy lookup.
- Use a vector to store the result and a string to store the current path.