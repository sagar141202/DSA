# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string will not have any leading zeros if the number is less than 10. For example, the input "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
This problem can be solved using recursion and backtracking. The algorithm will try to split the string into four parts, and for each part, it will check if it's a valid IP address segment. If it is, the algorithm will recursively try to split the remaining string.

## Complexity
- Time: O(3^N) where N is the length of the input string, because in the worst case, we might have to try all possible combinations of lengths for the four segments.
- Space: O(N) for storing the recursion stack.

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
    
    void backtrack(vector<string>& result, string& s, int start, vector<string> path) {
        if (path.size() == 4) {
            if (start == s.size()) {
                string ip = "";
                for (int i = 0; i < 4; i++) {
                    ip += path[i];
                    if (i < 3) ip += ".";
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
            backtrack(result, s, start + i, path);
            path.pop_back();
        }
    }
};

int main() {
    Solution solution;
    string input = "25525511135";
    vector<string> result = solution.restoreIpAddresses(input);
    for (auto ip : result) {
        cout << ip << endl;
    }
    return 0;
}
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
- The problem requires generating all possible combinations of valid IP addresses from a given string of digits.
- Recursion and backtracking are suitable approaches for solving this problem.
- It's essential to validate each segment to ensure it meets the conditions of a valid IP address segment.