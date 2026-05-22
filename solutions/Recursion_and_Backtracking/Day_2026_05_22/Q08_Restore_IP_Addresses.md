# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number should be between 0 and 255. For example, "25525511135" can be restored as ["255.255.11.135", "255.255.111.35"]. The input string is guaranteed to be non-empty and contains only digits.

## Approach
The approach to solve this problem is to use backtracking to generate all possible combinations of IP addresses. We will iterate over the string and try to form four numbers, checking if each number is valid (i.e., between 0 and 255). If a valid combination is found, we add it to the result list.

## Complexity
- Time: O(3^n) where n is the length of the string, as we are trying all possible combinations
- Space: O(n) for storing the recursive call stack and the result list

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
                for (int i = 0; i < path.size(); i++) {
                    ip += path[i];
                    if (i < path.size() - 1) ip += ".";
                }
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string segment = s.substr(start, i);
            if ((segment.size() > 1 && segment[0] == '0') || stoi(segment) > 255) continue;
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
- Use backtracking to generate all possible combinations of IP addresses.
- Check if each segment of the IP address is valid (i.e., between 0 and 255).
- Use a recursive function to generate all possible combinations and store the result in a list.