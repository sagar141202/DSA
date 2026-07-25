# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path and return the resulting path. The path starts with a slash '/' and may contain multiple slashes. The simplification process involves handling the '..' and '.' directories. The '..' directory moves up one level, while the '.' directory stays at the same level. For example, "/home/" simplifies to "/home", "/../" simplifies to "/", and "/home//foo/" simplifies to "/home/foo". The path is guaranteed to be a valid Unix path.

## Approach
We will utilize a stack to store the directories in the path. When we encounter a '..', we pop the last directory from the stack, and when we encounter a '.', we skip it. We then join the remaining directories in the stack with '/' to form the simplified path.

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
        string dir = "";
        for (char c : path) {
            if (c == '/') {
                if (dir != "") {
                    directories.push_back(dir);
                    dir = "";
                }
            } else {
                dir += c;
            }
        }
        if (dir != "") {
            directories.push_back(dir);
        }

        // Use a stack to simplify the path
        stack<string> stack;
        for (string directory : directories) {
            if (directory == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (directory != "" && directory != ".") {
                stack.push(directory);
            }
        }

        // Join the directories in the stack
        string simplifiedPath = "";
        while (!stack.empty()) {
            simplifiedPath = "/" + stack.top() + simplifiedPath;
            stack.pop();
        }
        if (simplifiedPath == "") {
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
- Use a stack to store the directories and handle the '..' and '.' directories.
- Split the path into directories and process each directory separately.
- Join the remaining directories in the stack to form the simplified path.