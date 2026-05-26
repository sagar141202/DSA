# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made of directories separated by '/' and '.' represents the current directory, while '..' represents the parent directory. The function should take a string path as input and return the simplified path as a string. For example, "/home/" should be simplified to "/home", "/../" should be simplified to "/", and "/home//foo/" should be simplified to "/home/foo". The path only contains letters, '.', '..', '/' and is not null.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, and if the directory is '..', it pops the last directory from the stack if it's not empty. If the directory is not '.' or '', it pushes the directory to the stack. Finally, it constructs the simplified path from the stack.

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
        string directory;
        for (char c : path) {
            if (c == '/') {
                if (!directory.empty()) {
                    directories.push_back(directory);
                    directory.clear();
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
            } else if (dir != "" && dir != ".") {
                stack.push(dir);
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
- Handle '..' by popping the last directory from the stack if it's not empty.
- Handle '.' by ignoring it.
- Construct the simplified path from the stack by prepending each directory with '/'.