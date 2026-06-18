# Simplify Path

## Problem Statement
Given an absolute path in a file system, simplify it by removing any redundant directories (i.e., directories that are followed by '..') and return the simplified path. The path is guaranteed to start with a forward slash ('/'). There will be no whitespace in the path. Furthermore, the path will not end with a slash ('/'). The path will contain at least one forward slash ('/') and will not start with two forward slashes ('//'). The path will not contain any dot ('.') directories. Examples of absolute paths that need simplification are "/home/", "/../", "/home//foo/". The output for these examples should be "/home", "/", and "/home/foo" respectively.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates over each directory in the path, and if the directory is not ".." or ".", it pushes the directory onto the stack. If the directory is "..", it pops the last directory from the stack. This approach ensures that any redundant directories are removed from the path.

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
- Use a stack to keep track of the directories in the path.
- Handle the ".." directory by popping the last directory from the stack.
- Handle the "." directory by ignoring it.
- Build the simplified path by iterating over the directories in the stack.