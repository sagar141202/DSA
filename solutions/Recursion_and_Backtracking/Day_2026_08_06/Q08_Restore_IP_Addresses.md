# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string will not have any leading zeros, and the length of the string will be between 4 and 12.

## Approach
We will use backtracking to generate all possible combinations of IP addresses. The algorithm will iterate over the string, creating all possible IP address segments and checking if they are valid. If a segment is valid, it will be added to the current combination, and the algorithm will move on to the next segment.

## Complexity
- Time: O(2^N * N) where N is the length of the string, as in the worst case, we might have to generate all possible combinations of IP addresses.
- Space: O(N) for storing the current combination of IP address segments.

## C++ Solution
```cpp
#include <vector>
#include <string>

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        vector<string> current;
        backtrack(s, 0, current, result);
        return result;
    }
    
    void backtrack(string& s, int start, vector<string>& current, vector<string>& result) {
        if (current.size() == 4) {
            if (start == s.size()) {
                string ip;
                for (int i = 0; i < current.size(); i++) {
                    ip += current[i];
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
            current.push_back(segment);
            backtrack(s, start + len, current, result);
            current.pop_back();
        }
    }
};
```

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

## Key Takeaways
- Use backtracking to generate all possible combinations of IP addresses.
- Check the validity of each segment by ensuring it does not start with a zero (unless it is zero itself) and its value is not greater than 255.
- Use a recursive approach to simplify the backtracking process and avoid unnecessary complexity.