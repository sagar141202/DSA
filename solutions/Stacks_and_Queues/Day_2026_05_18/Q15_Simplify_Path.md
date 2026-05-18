# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The function should take a string path as input and return a string representing the simplified path. For example, "/home/" should be simplified to "/home", "/../" should be simplified to "/", and "/home//foo/" should be simplified to "/home/foo". The path only consists of letters, digits, '/', '.', and '..'.

## Approach
We will use a stack to keep track of the directories in the path. When we encounter '..', we pop the last directory from the stack if it is not empty. When we encounter '.', we skip it. Otherwise, we push the directory into the stack.

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
- Handle '..' and '.' separately to simplify the path correctly.
- Build the simplified path by popping directories from the stack.