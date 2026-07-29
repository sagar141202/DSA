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
A number could represent multiple letters and each letter can only be used once in a combination. Return all possible combinations in any order.

## Approach
The problem can be solved using recursion and backtracking. Start by defining a mapping between digits and their corresponding letters, then iterate over each digit in the input string and recursively generate all possible combinations.

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case (when the input string consists of 7s and 9s), each digit can map to 4 letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Define the mapping between digits and letters
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

        vector<string> output;
        if (digits.empty()) return output;

        // Start the backtracking process
        backtrack(output, phone, digits, 0, "");
        return output;
    }

    void backtrack(vector<string>& output, unordered_map<char, string>& phone, string& digits, int index, string current) {
        // Base case: if we have processed all digits, add the current combination to the output
        if (index == digits.size()) {
            output.push_back(current);
            return;
        }

        // Get the letters corresponding to the current digit
        string letters = phone[digits[index]];

        // Recursively generate all possible combinations
        for (char letter : letters) {
            // Add the current letter to the current combination and move to the next digit
            backtrack(output, phone, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    string input = "23";
    vector<string> result = solution.letterCombinations(input);
    for (const string& combination : result) {
        cout << combination << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: 
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- Recursion and backtracking can be used to solve problems that involve generating all possible combinations of elements.
- The time complexity of the solution depends on the number of possible combinations, which can be exponential in the size of the input.
- The space complexity depends on the maximum depth of the recursion stack, which can be linear in the size of the input.