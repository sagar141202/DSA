# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made of directories separated by '/'. Here are the rules to simplify the path: 
1. '.' means the current directory, so it can be ignored.
2. '..' means the parent directory, so it can be ignored if the current directory is the root directory; otherwise, the last directory should be removed.
The path is guaranteed to start with '/' and only contains letters, '/' and '.' and '..'.
For example, "/home/", "/../", "/home//foo/", and "/a/./b/../../c/" are all valid paths.
The output should be the simplified path.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory, ignoring '.' and handling '..' by popping the last directory from the stack if it's not empty. The simplified path is then constructed from the stack.

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
                if (!dir.empty()) {
                    directories.push_back(dir);
                    dir = "";
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
                // Handle '..' by popping the last directory from the stack
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (directory != "." && !directory.empty()) {
                // Ignore '.' and empty directories
                stack.push(directory);
            }
        }

        // Construct the simplified path from the stack
        string simplifiedPath = "";
        while (!stack.empty()) {
            simplifiedPath = "/" + stack.top() + simplifiedPath;
            stack.pop();
        }

        // Handle the case where the simplified path is empty
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
- Use a stack to store the directories in the path to efficiently handle '..' and '.'.
- Ignore '.' and empty directories when constructing the simplified path.
- Handle the case where the simplified path is empty by returning '/'.