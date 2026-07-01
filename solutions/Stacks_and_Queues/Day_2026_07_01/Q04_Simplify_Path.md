# Simplify Path

## Problem Statement
Given an absolute path to a file, simplify the path by resolving the "." and ".." directories. The "." directory refers to the current directory, and the ".." directory refers to the parent directory. The path is simplified by removing any redundant "." directories and resolving any ".." directories. For example, "/home/", "/../", "/./" should be simplified to "/home", "/", and "/" respectively. The input path is guaranteed to be a valid Unix-style absolute path.

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates through each directory in the path, and if the directory is "..", it pops the last directory from the stack. If the directory is not "." or "..", it pushes the directory onto the stack. The simplified path is then constructed from the directories in the stack.

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
        string directory;
        vector<string> directories;
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
Input: "/./"
Output: "/"
Input: "/a/./b/../../c/"
Output: "/c"
```

## Key Takeaways
- Use a stack to keep track of the directories in the path.
- Iterate through each directory in the path and resolve any ".." directories by popping the last directory from the stack.
- Construct the simplified path from the directories in the stack.