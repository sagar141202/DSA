# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers (each representing a byte) separated by dots. Each number must be between 0 and 255, inclusive, and must not have leading zeros (unless the number is 0). For example, "25525511135" can be restored as ["255.255.11.135", "255.255.111.35"].

## Approach
We will use backtracking to generate all possible combinations of IP addresses. The algorithm will iterate through the string, generating all possible valid IP address parts and combining them to form valid IP addresses.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as in the worst case we might have to consider two possibilities for each character, and we have four parts in an IP address.
- Space: O(n) for the recursion stack and storing the result.

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
        
        for (int len = 1; len <= 3; len++) {
            if (start + len > s.size()) break;
            string part = s.substr(start, len);
            if ((part.size() > 1 && part[0] == '0') || stoi(part) > 255) continue;
            path.push_back(part);
            backtrack(result, s, start + len, path);
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
- Be careful with the constraints on IP address parts (no leading zeros unless the number is 0, and the number must be between 0 and 255).
- Use a helper function to perform the backtracking and store the result in the main function.