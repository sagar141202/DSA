# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is 0 itself. For example, given the string "25525511135", the output should be ["255.255.11.135", "255.255.111.35"].

## Approach
We will use a backtracking approach to generate all possible combinations of IP addresses. The algorithm will try to split the string into four parts, and for each part, it will check if the number is valid. If the number is valid, it will recursively try to split the remaining string.

## Complexity
- Time: O(2^N * N)
- Space: O(N)

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
    
    void backtrack(vector<string>& result, string& s, int start, vector<string> current) {
        if (current.size() == 4) {
            if (start == s.size()) {
                string ip;
                for (int i = 0; i < current.size(); i++) {
                    ip += current[i];
                    if (i < current.size() - 1) ip += ".";
                }
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string segment = s.substr(start, i);
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) continue;
            current.push_back(segment);
            backtrack(result, s, start + i, current);
            current.pop_back();
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
- The backtracking approach allows us to efficiently explore all possible combinations of IP addresses.
- We use a helper function `backtrack` to recursively try to split the string into four parts.
- We use a vector `current` to store the current combination of segments, and a vector `result` to store the final result.