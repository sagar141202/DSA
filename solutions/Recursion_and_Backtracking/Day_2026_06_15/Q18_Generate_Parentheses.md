# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parenthesis is one in which every open parenthesis can be matched with a corresponding closed parenthesis. The constraints are: `1 <= n <= 20`. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible combinations of parentheses by adding open and close parentheses at each step, and backtrack when the combination is not well-formed. The base case for the recursion is when the length of the current combination is equal to `2n`.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers
- Space: O(4^n / n^(3/2)) for storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack(result, "", 0, 0, n);
        return result;
    }
    
    void backtrack(vector<string>& result, string current, int open, int close, int max) {
        // if the length of the current combination is equal to 2n, add it to the result
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }
        
        // add open parenthesis if the number of open parentheses is less than n
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }
        
        // add close parenthesis if the number of close parentheses is less than the number of open parentheses
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
        }
    }
};

int main() {
    Solution solution;
    vector<string> result = solution.generateParenthesis(3);
    for (const auto& str : result) {
        cout << str << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- The base case for the recursion is when the length of the current combination is equal to `2n`.
- The time and space complexity are both O(4^n / n^(3/2)) due to the nature of Catalan numbers.