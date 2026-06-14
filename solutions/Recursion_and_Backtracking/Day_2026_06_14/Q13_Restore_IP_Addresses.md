# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255 (inclusive) without leading zeros (except for the number 0 itself). For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The approach involves using recursion and backtracking to generate all possible combinations of IP addresses. We will iterate over the string, considering each possible length for the four parts of the IP address, and check if the resulting combination is valid.

## Complexity
- Time: O(2^n * 4) where n is the length of the string, as in the worst case, we have 2 choices for the length of each part and we have 4 parts.
- Space: O(n) for storing the recursive call stack.

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
                string ip = path[0] + "." + path[1] + "." + path[2] + "." + path[3];
                result.push_back(ip);
            }
            return;
        }

        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string segment = s.substr(start, i);
            if ((segment.size() > 1 && segment[0] == '0') || stoi(segment) > 255) continue;
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
- Recursion and backtracking can be used to generate all possible combinations of IP addresses.
- We need to consider the constraints of a valid IP address, such as the length of each part and the absence of leading zeros.
- The time complexity is exponential due to the recursive nature of the solution, but it can be optimized by pruning the search space based on the constraints.