# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made of directories separated by '/' and '.' represents the current directory and '..' represents the parent directory. For example, "/../" should be simplified to "/", "/home/" should be simplified to "/home", and "/home//foo/" should be simplified to "/home/foo". The function should handle edge cases such as an empty path, a path with only '/' characters, or a path with consecutive '/' characters.

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates over each directory in the path, and if the directory is '..', it pops the last directory from the stack if the stack is not empty. If the directory is not '.' or '', it pushes the directory onto the stack. Finally, it constructs the simplified path from the directories in the stack.

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

        // Use a stack to keep track of the directories
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
- Use a stack to keep track of the directories in the path.
- Handle edge cases such as an empty path, a path with only '/' characters, or a path with consecutive '/' characters.
- Use a vector to split the path into directories and then iterate over each directory to simplify the path.