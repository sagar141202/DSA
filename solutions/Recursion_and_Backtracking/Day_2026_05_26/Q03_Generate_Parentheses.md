# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number of pairs. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, given the number of pairs as 3, the output should be all possible combinations of well-formed parentheses, such as ((())), (()()), (())(), ()(()), ()()(). The input is an integer n, representing the number of pairs of parentheses, and the output is a list of strings, each representing a well-formed combination of parentheses.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of well-formed parentheses. It starts with an empty string and adds open and close parentheses recursively, ensuring that the number of close parentheses never exceeds the number of open parentheses. This approach ensures that all generated combinations are well-formed.

## Complexity
- Time: O(4^n / n^(3/2))
- Space: O(4^n / n^(3/2))

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
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }
        
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }
        
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
        }
    }
};

int main() {
    Solution solution;
    int n = 3;
    vector<string> result = solution.generateParenthesis(n);
    for (const auto& str : result) {
        cout << str << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 3
Output: 
((()))
(()())
(())()
()(())
()()()
```

## Key Takeaways
- The recursive approach allows for efficient generation of all possible combinations of well-formed parentheses.
- The backtracking technique ensures that the solution explores all possible branches and avoids duplicate combinations.
- The time and space complexity are optimized by using a recursive approach with backtracking, resulting in a time complexity of O(4^n / n^(3/2)) and a space complexity of O(4^n / n^(3/2)).