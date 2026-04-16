# Simplify Path

## Problem Statement
Given an absolute path to a file, simplify it by removing any redundant directories (i.e., directories that can be reached by going up a level). The path is represented as a string, and it may contain multiple consecutive slashes. For example, "/home/" is the same as "/home". The path will not contain any files, only directories. The input path will always start with a slash. Return the simplified path.

## Approach
Use a stack to keep track of the directories in the path. Iterate over each directory in the path, and if it is "..", pop the last directory from the stack if it is not empty. If it is ".", skip it. Otherwise, add it to the stack. Finally, construct the simplified path from the directories in the stack.

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

        // Use a stack to keep track of the directories
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
Input: "/a/./b/../../c/"
Output: "/c"
```

## Key Takeaways
- Use a stack to keep track of the directories in the path.
- Handle the ".." and "." directories specially.
- Construct the simplified path from the directories in the stack.