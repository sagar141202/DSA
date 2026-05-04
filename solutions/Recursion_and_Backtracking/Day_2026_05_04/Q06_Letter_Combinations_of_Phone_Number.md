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
Each digit can only be used once, and the order of the letters matters.
Example: Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

## Approach
This problem can be solved using recursion and backtracking. We will use a recursive function to try all possible combinations of letters for each digit. The base case will be when we have tried all digits, at which point we add the current combination to the result list. We will use a map to store the mapping of digits to letters.

## Complexity
- Time: O(4^n) where n is the length of the input string, because in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursion stack and O(4^n) for storing the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> result;
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
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, unordered_map<char, string>& phone, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        for (char c : phone[digits[index]]) {
            backtrack(result, phone, digits, index + 1, current + c);
        }
    }
};

int main() {
    Solution solution;
    vector<string> result = solution.letterCombinations("23");
    for (const string& str : result) {
        cout << str << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Key Takeaways
- Recursion and backtracking can be used to solve problems that require trying all possible combinations of something.
- The use of a map can simplify the code and make it more readable when dealing with a fixed mapping.
- The time complexity of the solution is dependent on the number of possible combinations, which can be large for certain inputs.