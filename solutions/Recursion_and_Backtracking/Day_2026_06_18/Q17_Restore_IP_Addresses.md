# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255. The input string should not have any leading zeros, unless the number is zero itself. For example, given the input string "25525511135", the output should be ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses backtracking to generate all possible combinations of IP addresses. It checks each possible combination to ensure the numbers are between 0 and 255 and do not have leading zeros. The algorithm iterates over the string, considering all possible lengths for each segment of the IP address.

## Complexity
- Time: O(2^n * n) where n is the length of the input string, due to the backtracking and string concatenation
- Space: O(n) for the recursive call stack and storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(s, 0, result, {});
        return result;
    }
    
    void backtrack(string& s, int start, vector<string>& result, vector<string> path) {
        if (path.size() == 4) {
            if (start == s.size()) {
                string ip;
                for (int i = 0; i < 4; i++) {
                    ip += path[i];
                    if (i < 3) ip += ".";
                }
                result.push_back(ip);
            }
            return;
        }
        
        for (int len = 1; len <= 3; len++) {
            if (start + len > s.size()) break;
            string segment = s.substr(start, len);
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) continue;
            path.push_back(segment);
            backtrack(s, start + len, result, path);
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
- Use backtracking to generate all possible combinations of IP addresses
- Check each segment of the IP address to ensure it is between 0 and 255 and does not have leading zeros
- Use a recursive approach to simplify the code and avoid duplicate work.