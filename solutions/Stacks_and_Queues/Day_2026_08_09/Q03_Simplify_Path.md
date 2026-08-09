# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path by resolving the dots (`.` and `..`). The path is a string that starts with a forward slash (`/`) and consists of a sequence of directories separated by forward slashes. The `.` directory refers to the current directory, and the `..` directory refers to the parent directory. The function should return the simplified path.

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates over each directory in the path, and if the directory is not a dot, it pushes the directory onto the stack. If the directory is a dot, it does nothing. If the directory is a parent directory, it pops the last directory from the stack if the stack is not empty.

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
        string currentDirectory = "";
        for (char c : path) {
            if (c == '/') {
                if (!currentDirectory.empty()) {
                    directories.push_back(currentDirectory);
                    currentDirectory = "";
                }
            } else {
                currentDirectory += c;
            }
        }
        if (!currentDirectory.empty()) {
            directories.push_back(currentDirectory);
        }

        // Use a stack to simplify the path
        stack<string> stack;
        for (string directory : directories) {
            if (directory == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (directory != "." && !directory.empty()) {
                stack.push(directory);
            }
        }

        // Build the simplified path
        string simplifiedPath = "/";
        while (!stack.empty()) {
            simplifiedPath += stack.top() + "/";
            stack.pop();
        }
        if (simplifiedPath != "/") {
            simplifiedPath.pop_back();
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
- Use a stack to keep track of the directories in the path.
- Handle the `.` and `..` directories separately.
- Build the simplified path by popping directories from the stack.