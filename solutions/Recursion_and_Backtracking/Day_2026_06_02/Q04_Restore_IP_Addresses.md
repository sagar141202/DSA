# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string will not exceed 12 characters, and there will not be any leading zeros except for the number 0 itself. For example, the input "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
We will use a backtracking approach to generate all possible IP address combinations. The algorithm will iterate over the input string, trying all possible lengths for each segment of the IP address. We will use a helper function to validate each segment and ensure it meets the IP address criteria.

## Complexity
- Time: O(2^N * 4) where N is the length of the input string, as we are generating all possible combinations and validating each segment.
- Space: O(N) for storing the result and the recursion stack.

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
    
    void backtrack(string& s, int index, vector<string>& path, vector<string>& result) {
        if (path.size() == 4) {
            if (index == s.size()) {
                string ip = path[0];
                for (int i = 1; i < 4; i++) {
                    ip += "." + path[i];
                }
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (index + i > s.size()) break;
            string segment = s.substr(index, i);
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) continue;
            path.push_back(segment);
            backtrack(s, index + i, path, result);
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
- Validate each segment to ensure it meets the IP address criteria (between 0 and 255, inclusive, and no leading zeros).
- Use a helper function to recursively generate all possible combinations and validate each segment.