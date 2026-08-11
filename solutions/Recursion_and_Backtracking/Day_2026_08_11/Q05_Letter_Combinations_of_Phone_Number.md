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
Each digit can only be used once in a combination, and the order of combinations does not matter. 
For example, given the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We can use recursion and backtracking to generate all possible combinations. We will create a recursive function that tries each possible letter for the current digit and then recursively generates combinations for the remaining digits. 
The base case for the recursion is when there are no more digits to process, at which point we add the current combination to the result list. 
We will use a dictionary to map each digit to its corresponding letters.

## Complexity
- Time: O(4^n) where n is the length of the input string, because in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursive call stack, where n is the length of the input string.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

void backtrack(string& digits, int start, string& path, vector<string>& result) {
    if (start == digits.size()) {
        result.push_back(path);
        return;
    }
    for (char c : phone[digits[start]]) {
        path.push_back(c);
        backtrack(digits, start + 1, path, result);
        path.pop_back();
    }
}

vector<string> letterCombinations(string digits) {
    vector<string> result;
    if (digits.empty()) return result;
    string path;
    backtrack(digits, 0, path, result);
    return result;
}

int main() {
    string digits = "23";
    vector<string> result = letterCombinations(digits);
    for (string str : result) {
        cout << str << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Input: ""
Output: []
Input: "2"
Output: ["a", "b", "c"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters for a given phone number.
- Create a dictionary to map each digit to its corresponding letters for efficient lookup.
- Use a recursive function to try each possible letter for the current digit and then recursively generate combinations for the remaining digits.