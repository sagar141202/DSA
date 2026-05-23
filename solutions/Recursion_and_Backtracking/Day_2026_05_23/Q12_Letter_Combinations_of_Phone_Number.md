# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]. The mapping is as follows: 2 -> "abc", 3 -> "def", 4 -> "ghi", 5 -> "jkl", 6 -> "mno", 7 -> "pqrs", 8 -> "tuv", 9 -> "wxyz". The input will be a non-empty string of digits, and the length of the input will not exceed 4.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will iterate through each digit in the input string and for each digit, we will iterate through its corresponding letters. We will use a recursive function to generate all possible combinations.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, as in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> result;
        string mapping[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, digits, mapping, 0, "");
        return result;
    }

    void backtrack(vector<string>& result, string& digits, string mapping[], int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        for (char c : mapping[digits[index] - '0']) {
            backtrack(result, digits, mapping, index + 1, current + c);
        }
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
- Use a mapping array to store the letters corresponding to each digit.
- The time complexity is exponential due to the recursive nature of the solution.