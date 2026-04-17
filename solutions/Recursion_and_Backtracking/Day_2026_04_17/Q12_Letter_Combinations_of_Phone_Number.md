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
For example, input "23" would return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
The problem can be solved using recursion and backtracking. We start with an empty string and recursively append all possible letters for each digit. When we have processed all digits, we add the current combination to the result list.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, as in the worst case (for digit 7 or 9), we have 4 possible letters for each digit.
- Space: O(n) for the recursive call stack, where n is the number of digits in the input string.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> result;
        vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, "", digits, 0, mapping);
        return result;
    }
    
    void backtrack(vector<string>& result, string current, string& digits, int index, vector<string>& mapping) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        string letters = mapping[digits[index] - '0'];
        for (char letter : letters) {
            backtrack(result, current + letter, digits, index + 1, mapping);
        }
    }
};

int main() {
    Solution solution;
    string input = "23";
    vector<string> output = solution.letterCombinations(input);
    for (const auto& str : output) {
        cout << str << " ";
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
- Recursion and backtracking can be used to solve problems involving combinations and permutations.
- The key to solving this problem is to define a recursive function that takes the current combination and the remaining digits as arguments.
- The base case for the recursion is when all digits have been processed, at which point the current combination is added to the result list.