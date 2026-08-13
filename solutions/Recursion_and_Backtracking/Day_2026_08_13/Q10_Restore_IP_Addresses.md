# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255. The input string must not contain any leading zeros for numbers greater than 0, unless the number itself is 0. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses recursion and backtracking to generate all possible combinations of IP addresses. It iterates over the input string, considering all possible lengths for the first part of the IP address, and then recursively generates the remaining parts. The algorithm checks if each part is a valid IP address segment.

## Complexity
- Time: O(2^N * 4) where N is the length of the input string, as in the worst case, we might have to consider two possibilities for each character (being part of the current segment or not), and we have four segments in an IP address.
- Space: O(N) for storing the recursive call stack and the current IP address being constructed.

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
        backtrack(result, path, s, 0);
        return result;
    }
    
    void backtrack(vector<string>& result, vector<string>& path, string& s, int start) {
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
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) {
                continue;
            }
            path.push_back(segment);
            backtrack(result, path, s, start + i);
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
- The key to solving this problem is understanding how to use recursion and backtracking to generate all possible combinations of IP addresses.
- It's crucial to validate each segment of the IP address to ensure it's within the valid range (0-255) and doesn't have leading zeros unless it's zero itself.
- The use of a path vector to store the current segments being considered helps in efficiently exploring all possible combinations without redundant computations.