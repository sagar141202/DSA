# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is zero itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The approach involves using recursion and backtracking to generate all possible combinations of four numbers from the input string. We will use a helper function to check if a substring can be a valid IP address segment.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as we are generating all possible substrings and checking for validity.
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

    void backtrack(string& s, int start, vector<string>& path, vector<string>& result) {
        if (path.size() == 4) {
            if (start == s.size()) {
                string ip = path[0];
                for (int i = 1; i < 4; i++) {
                    ip += "." + path[i];
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
- Use recursion and backtracking to generate all possible combinations of IP address segments.
- Validate each segment to ensure it does not have leading zeros and is within the range of 0 to 255.
- Use a helper function to check the validity of each segment and to backtrack when necessary.