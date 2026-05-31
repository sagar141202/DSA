# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path by removing any redundant directories (i.e., directories that are followed by ".." which means "go to parent directory") and "." which means "stay in the same directory". The path starts with a "/", and all directories in the path are separated by "/". The output should be the simplified absolute path. For example, given the path "/home/", the function should return "/home". Given the path "/../", the function should return "/". Given the path "/home//foo/", the function should return "/home/foo". Given the path "/a/./b/../../c/", the function should return "/c".

## Approach
The algorithm uses a stack to store the directories in the path. It iterates through each directory in the path, and if the directory is "..", it pops the last directory from the stack if the stack is not empty. If the directory is ".", it skips it. Otherwise, it pushes the directory into the stack. Finally, it constructs the simplified path from the directories in the stack.

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
            } else if (dir != "." && !dir.empty()) {
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
Input: "/a/./b/../../c/"
Output: "/c"
```

## Key Takeaways
- Use a stack to store the directories in the path to efficiently handle ".." and ".".
- Split the path into directories and iterate through each directory to simplify the path.
- Construct the simplified path from the directories in the stack.