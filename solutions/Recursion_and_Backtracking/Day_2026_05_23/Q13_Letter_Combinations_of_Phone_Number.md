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
A number could represent multiple letters, and each letter combination is a solution. Note that the input will not contain any 0's or 1's, and the input string will not be empty.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of letters. It iterates over each digit in the input string, and for each digit, it iterates over the corresponding letters. The algorithm builds up the combinations by adding each letter to the current combination.

## Complexity
- Time: O(4^n) where n is the length of the input string, since each digit can have up to 4 possible letters
- Space: O(n) for the recursion stack

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
        cout << combination << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: 
"ad"
"ae"
"af"
"bd"
"be"
"bf"
"cd"
"ce"
"cf"
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters
- Use a vector to store the phone mapping and a vector to store the result
- The time complexity is O(4^n) due to the maximum of 4 possible letters per digit
- The space complexity is O(n) for the recursion stack