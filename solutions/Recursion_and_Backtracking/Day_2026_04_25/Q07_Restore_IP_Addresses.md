# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers (each between 0 and 255) separated by dots. The numbers cannot have leading zeros unless the number is zero itself. For example, "255.0.0.0" is a valid IP address, but "025.0.0.0" and "255.00.0.0" are not. The input string "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The problem can be solved using recursion and backtracking, where we generate all possible combinations of four numbers and check if each combination is a valid IP address. We use a helper function to validate each segment of the IP address.

## Complexity
- Time: O(3^n) where n is the length of the input string, as in the worst-case scenario, we are generating all possible combinations of the string.
- Space: O(n) for the recursion stack and storing the result.

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

    void backtrack(string &s, int start, vector<string> &path, vector<string> &result) {
        if (path.size() == 4) {
            if (start == s.length()) {
                string ip = path[0];
                for (int i = 1; i < 4; i++) {
                    ip += "." + path[i];
                }
                result.push_back(ip);
            }
            return;
        }

        for (int i = 1; i <= 3; i++) {
            if (start + i > s.length()) break;
            string segment = s.substr(start, i);
            if ((segment.length() > 1 && segment[0] == '0') || stoi(segment) > 255) continue;
            path.push_back(segment);
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
- Use recursion and backtracking to generate all possible combinations of IP addresses.
- Validate each segment of the IP address to ensure it does not have leading zeros and is within the valid range.
- Use a helper function to simplify the validation process and improve code readability.