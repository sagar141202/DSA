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
A number could represent multiple letters and each letter combination is a solution. For example, the input "23" could be "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", or "cf".

## Approach
The problem can be solved using recursion and backtracking, where each recursive call tries all possible letters for the current digit. The base case is when the input string is empty, at which point we add the current combination to the result. The algorithm iterates over all possible letters for each digit and recursively generates all combinations.

## Complexity
- Time: O(4^n) where n is the length of the input string, since each digit can have up to 4 possible letters.
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
        backtrack(result, digits, 0, "", mapping);
        return result;
    }

    void backtrack(vector<string>& result, string& digits, int index, string current, string mapping[]) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        string letters = mapping[digits[index] - '0'];
        for (char letter : letters) {
            backtrack(result, digits, index + 1, current + letter, mapping);
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
- Recursion and backtracking can be used to generate all possible combinations of letters for a given phone number.
- The time complexity is exponential due to the recursive nature of the algorithm.
- The space complexity is linear due to the recursion stack.