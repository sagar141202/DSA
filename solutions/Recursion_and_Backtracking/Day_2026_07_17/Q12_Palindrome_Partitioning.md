# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists only of lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The solution uses backtracking to generate all possible partitions of the input string and checks if each partition is a palindrome. The algorithm starts by checking all substrings of the input string to see if they are palindromes, then recursively generates all possible partitions.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        backtrack(result, path, s, 0);
        return result;
    }
    
    void backtrack(vector<vector<string>>& result, vector<string>& path, string& s, int start) {
        if (start == s.size()) {
            result.push_back(path);
            return;
        }
        
        for (int end = start; end < s.size(); end++) {
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                path.push_back(substr);
                backtrack(result, path, s, end + 1);
                path.pop_back();
            }
        }
    }
    
    bool isPalindrome(string& s) {
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
    string input = "aab";
    vector<vector<string>> result = solution.partition(input);
    for (auto& partition : result) {
        for (auto& substr : partition) {
            cout << substr << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: "aab"
Output: 
a a b 
aa b 
```

## Key Takeaways
- Use backtracking to generate all possible partitions of the input string.
- Check if each substring is a palindrome before adding it to the current partition.
- The time complexity is exponential due to the backtracking, but it is necessary to generate all possible partitions.