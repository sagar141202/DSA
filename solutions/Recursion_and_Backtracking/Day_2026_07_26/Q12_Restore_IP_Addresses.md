# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers (each between 0 and 255) separated by dots. The numbers cannot have leading zeros unless the number is 0 itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The solution uses backtracking to generate all possible combinations of four numbers from the input string, checking each combination to ensure it represents a valid IP address. It iterates through the string, creating segments of 1 to 3 digits, and checks if each segment is valid.

## Complexity
- Time: O(2^n * 4) where n is the length of the string, as in the worst case, we might have to try all possible combinations and each segment can have up to 3 digits.
- Space: O(n) for storing the recursive call stack and the current combination being checked.

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
                for (const auto& segment : current) {
                    ip += segment + ".";
                }
                ip.pop_back(); // Remove the trailing dot
                result.push_back(ip);
            }
            return;
        }

        for (int len = 1; len <= 3; ++len) {
            if (start + len > s.size()) break;
            std::string segment = s.substr(start, len);
            if ((segment[0] == '0' && segment.size() > 1) || std::stoi(segment) > 255) continue;
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
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

## Key Takeaways
- Ensure each segment of the IP address does not have leading zeros unless it is zero itself.
- Validate each segment to be between 0 and 255.
- Use backtracking to efficiently generate all possible combinations.