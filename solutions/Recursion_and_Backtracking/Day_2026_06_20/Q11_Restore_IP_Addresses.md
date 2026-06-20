# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers (each between 0 and 255) separated by dots. The given string should not have leading zeros in the IP address, unless the number is zero. For example, given the string "25525511135", the possible valid IP addresses are ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses backtracking to generate all possible combinations of four numbers from the given string. It checks each combination to ensure that it forms a valid IP address. The algorithm iterates through the string, considering all possible lengths for the first, second, third, and fourth parts of the IP address.

## Complexity
- Time: O(2^n * n) where n is the length of the string, as each character can be part of a new segment or not, and we need to validate each segment.
- Space: O(n) for storing the recursive call stack and the current IP address segments.

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

        for (int len = 1; len <= 3; len++) {
            if (start + len > s.size()) break;
            string segment = s.substr(start, len);
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) continue;
            path.push_back(segment);
            backtrack(result, s, start + len, path);
            path.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<string> result = solution.restoreIpAddresses("25525511135");
    for (auto& ip : result) {
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
- Use backtracking to generate all possible combinations of four numbers from the given string.
- Check each combination to ensure that it forms a valid IP address by verifying that each segment is between 0 and 255 and does not have leading zeros unless the number is zero.
- Use recursion to explore all possible combinations and store the valid IP addresses in a result vector.