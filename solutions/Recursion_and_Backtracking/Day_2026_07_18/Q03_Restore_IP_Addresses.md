# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not contain any leading zeros, unless the number is zero itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations of four numbers from the input string. We will iterate over the string, considering each substring as a potential part of the IP address, and then recursively generate the rest of the address.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as in the worst case, we might have to consider two possibilities for each character (being part of the current segment or not) and we have four segments in an IP address.
- Space: O(n) for storing the recursive call stack and the current IP address segments.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
                for (int i = 0; i < 3; i++) {
                    ip += current[i] + ".";
                }
                ip += current[3];
                result.push_back(ip);
            }
            return;
        }
        
        for (int len = 1; len <= 3; len++) {
            if (start + len > s.size()) break;
            string segment = s.substr(start, len);
            if ((segment.size() > 1 && segment[0] == '0') || stoi(segment) > 255) {
                continue;
            }
            current.push_back(segment);
            backtrack(s, start + len, current, result);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    string input = "25525511135";
    vector<string> output = solution.restoreIpAddresses(input);
    for (const auto& ip : output) {
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
- The key to solving this problem is to use recursion and backtracking to explore all possible combinations of IP address segments.
- We need to ensure that each segment is between 0 and 255, inclusive, and does not have leading zeros unless it is zero itself.
- The time complexity is exponential due to the recursive nature of the solution, but it is necessary to explore all possible combinations.