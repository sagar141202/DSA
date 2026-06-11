# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '.' and '..' directories. The path is simplified by resolving the '.' directories (which represent the current directory) and the '..' directories (which represent the parent directory). For example, "/home/" and "/../" are equivalent to "/". The path is guaranteed to start with a '/', and only contains letters, '.', and '/'. There will be no consecutive '/' characters.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over the path, pushing directories onto the stack and popping them when it encounters '..'. The simplified path is then constructed from the directories left in the stack. This approach ensures that the path is simplified correctly and efficiently.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        // Split the path into directories
        vector<string> directories;
        string directory = "";
        for (char c : path) {
            if (c == '/') {
                if (!directory.empty()) {
                    directories.push_back(directory);
                    directory = "";
                }
            } else {
                directory += c;
            }
        }
        if (!directory.empty()) {
            directories.push_back(directory);
        }

        // Use a stack to simplify the path
        stack<string> stack;
        for (string dir : directories) {
            if (dir == "." || dir == "") {
                continue;
            } else if (dir == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else {
                stack.push(dir);
            }
        }

        // Construct the simplified path
        string simplifiedPath = "";
        while (!stack.empty()) {
            simplifiedPath = "/" + stack.top() + simplifiedPath;
            stack.pop();
        }
        if (simplifiedPath.empty()) {
            return "/";
        }
        return simplifiedPath;
    }
};
```

## Test Cases
```
Input: "/home/"
Output: "/home"
Input: "/../"
Output: "/"
Input: "/home//foo/"
Output: "/home/foo"
```

## Key Takeaways
- Use a stack to efficiently simplify the path by resolving '.' and '..' directories.
- Handle edge cases such as consecutive '/' characters and empty directories.
- Construct the simplified path by iterating over the stack and appending directories to the result string.