# Simplify Path

## Problem Statement
Given an absolute path in a file system, simplify it by resolving '..' and '.' in the path. The path is guaranteed to start with a '/' and may or may not end with a '/'. Also, the path only contains letters, digits, '/', '.', and '..'. The function should return the simplified path. For example, "/home/" should return "/home", "/../" should return "/", and "/home//foo/" should return "/home/foo".

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, and if the directory is '..', it pops the last directory from the stack if it's not empty. If the directory is '.', it skips it. Otherwise, it pushes the directory to the stack.

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
        for (string dir : directories) {
            if (dir == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (dir != "." && !dir.empty()) {
                stack.push(dir);
            }
        }

        // Build the simplified path
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
- Use a stack to store the directories in the path.
- Handle '..' and '.' directories separately.
- Build the simplified path by popping directories from the stack.