# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not have any leading zeros, unless the number is zero itself. For example, the input string "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The problem can be solved using recursion and backtracking, where we generate all possible combinations of four numbers from the given string and check if each combination forms a valid IP address. The algorithm checks for valid IP address conditions at each step of recursion.

## Complexity
- Time: O(2^n * n) where n is the length of the string, due to generating all possible combinations and checking their validity.
- Space: O(n) for storing the recursive call stack and the current combination being generated.

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
                string ip = current[0] + "." + current[1] + "." + current[2] + "." + current[3];
                result.push_back(ip);
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string segment = s.substr(start, i);
            if ((segment.size() > 1 && segment[0] == '0') || stoi(segment) > 255) continue;
            current.push_back(segment);
            backtrack(s, start + i, current, result);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    string input = "25525511135";
    vector<string> result = solution.restoreIpAddresses(input);
    for (string ip : result) {
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
- Use recursion and backtracking to generate all possible combinations of IP address segments.
- Validate each segment to ensure it meets the conditions of a valid IP address.
- Use a vector to store the current combination being generated and another vector to store the final result.