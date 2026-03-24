# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, except for the number 0 itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
We can use backtracking to generate all possible combinations of four numbers. We will iterate over the string and consider all possible lengths for the first, second, third, and fourth parts of the IP address. We will use recursion to explore all possible combinations and validate each part to ensure it is a valid IP address segment.

## Complexity
- Time: O(2^N * 4) where N is the length of the input string
- Space: O(N) for storing the recursion stack and the current IP address segments

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
Output: ["255.255.11.135","255.255.111.35"]
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

## Key Takeaways
- Use backtracking to generate all possible combinations of four numbers.
- Validate each segment to ensure it is a valid IP address segment (between 0 and 255, no leading zeros except for 0 itself).
- Use recursion to explore all possible combinations and store the valid IP addresses in the result vector.