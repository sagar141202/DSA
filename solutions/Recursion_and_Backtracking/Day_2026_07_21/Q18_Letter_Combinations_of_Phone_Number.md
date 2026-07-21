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
For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We will use recursion and backtracking to generate all possible combinations of letters. We will iterate over each digit in the input string, and for each digit, we will recursively generate all possible combinations of the remaining digits. The base case for the recursion will be when the input string is empty, at which point we will add the current combination to the result list.

## Complexity
- Time: O(4^n) where n is the length of the input string, since in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursion stack, where n is the length of the input string.

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

int main() {
    Solution solution;
    string digits = "23";
    vector<string> result = solution.letterCombinations(digits);
    for (string combination : result) {
        cout << combination << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters.
- Use a base case to stop the recursion and add the current combination to the result list.
- Use a helper function to perform the backtracking and recursion.