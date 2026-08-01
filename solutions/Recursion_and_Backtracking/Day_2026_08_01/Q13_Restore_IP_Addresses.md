# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string should not have any leading zeros, unless the number is zero itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
We will use recursion and backtracking to generate all possible combinations of IP addresses. The algorithm will try to split the string into four parts, and for each part, it will check if the number is valid. If it is, the algorithm will continue with the next part. If not, it will backtrack and try a different split.

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
        vector<string> path;
        backtrack(s, path, result, 0);
        return result;
    }
    
    void backtrack(string& s, vector<string>& path, vector<string>& result, int start) {
        if (path.size() == 4) {
            if (start == s.size()) {
                string ip = path[0] + "." + path[1] + "." + path[2] + "." + path[3];
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string substr = s.substr(start, i);
            if ((substr.size() > 1 && substr[0] == '0') || stoi(substr) > 255) continue;
            path.push_back(substr);
            backtrack(s, path, result, start + i);
            path.pop_back();
        }
    }
};
```

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of IP addresses.
- Check if each part of the IP address is valid before continuing with the next part.
- Use a vector to store the current path and another vector to store the final result.