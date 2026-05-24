# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255. The input string should not have any leading zeros, and each number should not exceed three digits. For example, given the string "25525511135", the output should be ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses recursion and backtracking to generate all possible IP address combinations. It iterates over the input string, dividing it into four segments, and checks if each segment is a valid IP address part. If a valid combination is found, it is added to the result list.

## Complexity
- Time: O(2^n * n) where n is the length of the input string, due to the recursive nature of the solution
- Space: O(n) for storing the recursive call stack and the result list

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
                string ip = current[0] + "." + current[1] + "." + current[2] + "." + current[3];
                result.push_back(ip);
            }
            return;
        }
        
        for (int len = 1; len <= 3; len++) {
            if (start + len > s.size()) break;
            string segment = s.substr(start, len);
            if ((segment[0] == '0' && segment.size() > 1) || stoi(segment) > 255) continue;
            current.push_back(segment);
            backtrack(result, s, start + len, current);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    string input = "25525511135";
    vector<string> result = solution.restoreIpAddresses(input);
    for (const auto& ip : result) {
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
- Use recursion and backtracking to generate all possible IP address combinations
- Validate each segment to ensure it is a valid IP address part
- Use a vector to store the current combination and add it to the result list when a valid combination is found