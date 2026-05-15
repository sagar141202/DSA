# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is zero itself. For example, "25525511135" can be restored as ["255.255.11.135", "255.255.111.35"].

## Approach
The algorithm uses backtracking to generate all possible combinations of IP addresses. It iterates over the string, considering each substring as a potential part of the IP address. The algorithm checks if the current substring is a valid IP segment and then recursively generates the remaining segments.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as there are 2^n possible substrings and 4 segments in an IP address
- Space: O(n) for storing the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, s, 0, {});
        return result;
    }
    
    void backtrack(vector<string>& result, string& s, int start, vector<string> path) {
        if (path.size() == 4) {
            if (start == s.size()) {
                string ip = "";
                for (int i = 0; i < 4; i++) {
                    ip += path[i];
                    if (i < 3) ip += ".";
                }
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string segment = s.substr(start, i);
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) continue;
            path.push_back(segment);
            backtrack(result, s, start + i, path);
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
- Check each substring to ensure it's a valid IP segment (between 0 and 255, no leading zeros unless it's zero)
- Use recursion to generate the remaining segments of the IP address