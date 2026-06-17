# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The string `s` consists of lowercase English letters and has a length of at most 10. The goal is to return all possible palindrome partitions of `s`.

## Approach
The approach is to use backtracking to generate all possible partitions of the string and then check if each partition is a palindrome. The algorithm starts by choosing the first partition, then recursively chooses the next partition, and so on. If a partition is not a palindrome, the algorithm backtracks and tries a different partition.

## Complexity
- Time: O(2^n * n) where n is the length of the string, because in the worst case, we have to generate all possible partitions of the string and check if each partition is a palindrome.
- Space: O(n) for the recursive call stack and to store the current partition.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> current;
        backtrack(result, current, s, 0);
        return result;
    }
    
    void backtrack(vector<vector<string>>& result, vector<string>& current, string s, int start) {
        if (start == s.size()) {
            result.push_back(current);
            return;
        }
        
        for (int i = start; i < s.size(); i++) {
            string substr = s.substr(start, i - start + 1);
            if (isPalindrome(substr)) {
                current.push_back(substr);
                backtrack(result, current, s, i + 1);
                current.pop_back();
            }
        }
    }
    
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};

int main() {
    Solution solution;
    string s = "aab";
    vector<vector<string>> result = solution.partition(s);
    for (const auto& partition : result) {
        for (const auto& substr : partition) {
            cout << substr << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: s = "aab"
Output: 
a a b 
aa b 
```

## Key Takeaways
- The key to solving this problem is to use backtracking to generate all possible partitions of the string.
- Checking if a substring is a palindrome can be done by comparing characters from the start and end of the substring and moving towards the center.
- The time complexity is exponential because in the worst case, we have to generate all possible partitions of the string.