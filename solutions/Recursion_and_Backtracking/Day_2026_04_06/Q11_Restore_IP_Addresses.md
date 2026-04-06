# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not contain any leading zeros, unless the number is zero itself. For example, given the input string "25525511135", the output should be ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses recursion and backtracking to generate all possible combinations of valid IP addresses. It iterates over the input string, considering all possible lengths for the first part of the IP address, and then recursively generates the remaining parts. The algorithm ensures that each part of the IP address is a valid number between 0 and 255.

## Complexity
- Time: O(2^N * 4) where N is the length of the input string, since in the worst case, we might have to consider two possibilities for each character, and we have four parts in an IP address
- Space: O(N) for storing the recursive call stack and the current IP address being generated

## C++ Solution
```cpp
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> restoreIpAddresses(std::string s) {
        std::vector<std::string> result;
        std::vector<std::string> current;
        backtrack(s, 0, current, result);
        return result;
    }

    void backtrack(const std::string& s, int start, std::vector<std::string>& current, std::vector<std::string>& result) {
        if (current.size() == 4) {
            if (start == s.size()) {
                std::string ip;
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
            std::string substr = s.substr(start, len);
            if ((substr.size() > 1 && substr[0] == '0') || std::stoi(substr) > 255) continue;
            current.push_back(substr);
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
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

## Key Takeaways
- The solution uses recursion and backtracking to efficiently generate all possible valid IP addresses.
- It ensures that each part of the IP address is a valid number between 0 and 255 by checking for leading zeros and the maximum value.
- The time complexity is exponential due to the recursive nature of the solution, but it is necessary to consider all possible combinations of valid IP addresses.