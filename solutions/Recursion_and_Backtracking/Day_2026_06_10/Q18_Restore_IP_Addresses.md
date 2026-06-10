# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not contain any non-digit characters. For example, the input "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The approach is to use backtracking to generate all possible combinations of four numbers. We will iterate over the string and try to form a valid IP address by dividing it into four parts. We will use a helper function to check if a substring can be a valid part of an IP address.

## Complexity
- Time: O(2^n * n) where n is the length of the string, as we are generating all possible combinations
- Space: O(n) for the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        vector<string> path;
        backtrack(s, 0, path, result);
        return result;
    }

    void backtrack(string& s, int start, vector<string>& path, vector<string>& result) {
        if (path.size() == 4) {
            if (start == s.size()) {
                string ip;
                for (int i = 0; i < path.size(); i++) {
                    ip += path[i];
                    if (i < 3) ip += ".";
                }
                result.push_back(ip);
            }
            return;
        }

        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string substr = s.substr(start, i);
            if ((substr.size() > 1 && substr[0] == '0') || stoi(substr) > 255) continue;
            path.push_back(substr);
            backtrack(s, start + i, path, result);
            path.pop_back();
        }
    }
};
```

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

## Key Takeaways
- Use backtracking to generate all possible combinations of four numbers.
- Check if a substring can be a valid part of an IP address by ensuring it does not start with 0 (unless it is 0 itself) and its integer value is not greater than 255.
- Use a helper function to recursively build the IP address combinations.