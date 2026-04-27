# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path by resolving the "." and ".." directories. The "." directory refers to the current directory, and the ".." directory refers to the parent directory. The path is simplified by removing any redundant "." directories and resolving any ".." directories. For example, the path "/home/" is equivalent to "/home", and the path "/../" is equivalent to "/". The input path is guaranteed to be a valid Unix-style path.

## Approach
The algorithm uses a stack to store the directories in the path. It iterates through the path, pushing directories onto the stack and popping them off when it encounters a ".." directory. The simplified path is then constructed by joining the remaining directories in the stack.

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

        // Construct the simplified path
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
- Use a stack to simplify the path by resolving "." and ".." directories.
- Split the path into directories and iterate through them to simplify the path.
- Construct the simplified path by joining the remaining directories in the stack.