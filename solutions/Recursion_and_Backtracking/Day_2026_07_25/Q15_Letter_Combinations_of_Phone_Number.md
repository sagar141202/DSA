# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
- 2: 'a', 'b', 'c'
- 3: 'd', 'e', 'f'
- 4: 'g', 'h', 'i'
- 5: 'j', 'k', 'l'
- 6: 'm', 'n', 'o'
- 7: 'p', 'q', 'r', 's'
- 8: 't', 'u', 'v'
- 9: 'w', 'x', 'y', 'z'
A number could represent multiple letters, so each digit in the input string could map to multiple letters. For example, the input "23" could represent the words "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf". The order of the output does not matter.

## Approach
The problem can be solved using recursion and backtracking. We start with an empty string and try to append each possible letter to the current string. We then recursively call the function with the updated string and the remaining digits. If there are no more digits, we add the current string to the result list.

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case (for digit 7 or 9), each digit can map to 4 letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }

        vector<string> result;
        vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, mapping, digits, 0, "");
        return result;
    }

    void backtrack(vector<string>& result, vector<string>& mapping, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }

        string letters = mapping[digits[index] - '0'];
        for (char letter : letters) {
            backtrack(result, mapping, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    string input = "23";
    vector<string> result = solution.letterCombinations(input);
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
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters.
- Create a mapping of digits to letters to simplify the code.
- Use a helper function to perform the backtracking and add the resulting combinations to the result list.