# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made up of a sequence of directories and '.' represents the current directory, while '..' represents the parent directory. For example, "/home/" is equivalent to "/home", and "/../" is equivalent to "/". Also, "/home//foo/" is equivalent to "/home/foo". The function should return the simplified path.

## Approach
We will use a stack to store the directories in the path. When we encounter '..', we pop the last directory from the stack if it is not empty. When we encounter '.', we ignore it. Finally, we construct the simplified path from the directories in the stack.

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

        // Use a stack to store the directories
        stack<string> stack;
        for (string directory : directories) {
            if (directory == "..") {
                // If the stack is not empty, pop the last directory
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (directory != "" && directory != ".") {
                // Push the directory into the stack
                stack.push(directory);
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
```

## Key Takeaways
- Use a stack to store the directories in the path.
- Handle '..' and '.' correctly by popping the last directory from the stack or ignoring it.
- Construct the simplified path from the directories in the stack.