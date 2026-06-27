# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. Additionally, the first number cannot be 0 unless the entire number is 0. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses backtracking to generate all possible combinations of IP addresses. It tries to split the string into four parts, ensuring each part is a valid IP segment. The algorithm explores all possible splits and backtracks when a split is invalid.

## Complexity
- Time: O(2^n * 4) where n is the length of the string, as each character can be the start of a new segment and there are four segments in an IP address
- Space: O(n) for the recursion stack and storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(s, 0, {}, result);
        return result;
    }
    
    void backtrack(string& s, int start, vector<string> path, vector<string>& result) {
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
            backtrack(s, start + len, path, result);
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
- The backtracking approach allows us to explore all possible combinations of IP addresses.
- The validation of each segment ensures that only valid IP addresses are generated.
- The use of recursion and a vector to store the current path enables efficient exploration and construction of IP addresses.