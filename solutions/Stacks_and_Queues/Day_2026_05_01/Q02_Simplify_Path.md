# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made of directories separated by '/'. '..' means go to the parent directory, and '.' means stay in the same directory. For example, "/home/", "/../", "/home//foo/", and "/a/./b/../../c/" are all valid paths. The output should be the simplified path.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, and if the directory is '..', it pops the last directory from the stack. If the directory is '.', it skips it. Otherwise, it pushes the directory onto the stack.

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
        string dir;
        vector<string> dirs;
        for (char c : path) {
            if (c == '/') {
                if (!dir.empty()) {
                    dirs.push_back(dir);
                    dir.clear();
                }
            } else {
                dir += c;
            }
        }
        if (!dir.empty()) {
            dirs.push_back(dir);
        }

        // Use a stack to store the directories
        stack<string> stack;
        for (string d : dirs) {
            if (d == "..") {
                // Go to the parent directory
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (d == ".") {
                // Stay in the same directory
                continue;
            } else {
                // Add the directory to the stack
                stack.push(d);
            }
        }

        // Build the simplified path
        string simplifiedPath;
        while (!stack.empty()) {
            simplifiedPath = "/" + stack.top() + simplifiedPath;
            stack.pop();
        }

        // If the path is empty, return "/"
        if (simplifiedPath.empty()) {
            return "/";
        } else {
            return simplifiedPath;
        }
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
Input: "/a/./b/../../c/"
Output: "/c"
```

## Key Takeaways
- Use a stack to store the directories in the path.
- Handle '..' and '.' separately to simplify the path.
- Build the simplified path by popping directories from the stack.