# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is zero itself. For example, the input string "25525511135" can be restored as ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses recursion and backtracking to generate all possible valid IP address combinations. It iterates over the input string, generating all possible combinations of four numbers. The algorithm checks if each number is valid (between 0 and 255, inclusive, and does not have leading zeros unless it is zero itself).

## Complexity
- Time: O(2^N * 4) where N is the length of the input string, as in the worst case, we might need to explore all possible combinations of four numbers.
- Space: O(N) for storing the recursive call stack and the output.

## C++ Solution
```cpp
#include <vector>
#include <string>
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
- Use recursion and backtracking to generate all possible combinations of four numbers.
- Check each number for validity (between 0 and 255, inclusive, and does not have leading zeros unless it is zero itself).
- Use a vector to store the current path and another vector to store the final result.