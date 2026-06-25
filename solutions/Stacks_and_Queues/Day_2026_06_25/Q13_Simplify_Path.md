# Simplify Path

## Problem Statement
Given an absolute path in a file system, simplify the path by removing any redundant '.' or '..' directories. The path is a string that starts with a '/' and consists of a series of directories separated by '/'. The '.' directory refers to the current directory, and the '..' directory refers to the parent directory. For example, "/home/" is equivalent to "/home", and "/home/../" is equivalent to "/". The function should return the simplified path.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, and if the directory is '..', it pops the last directory from the stack if it is not empty. If the directory is not '.' or '..', it pushes the directory onto the stack. Finally, it constructs the simplified path by concatenating the directories in the stack.

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
        string dir;
        for (char c : path) {
            if (c == '/') {
                if (!dir.empty()) {
                    directories.push_back(dir);
                    dir.clear();
                }
            } else {
                dir += c;
            }
        }
        if (!dir.empty()) {
            directories.push_back(dir);
        }

        // Use a stack to store the directories
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

        // Construct the simplified path
        string simplifiedPath;
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
- Handle the '..' directory by popping the last directory from the stack if it is not empty.
- Handle the '.' directory by ignoring it.
- Construct the simplified path by concatenating the directories in the stack.