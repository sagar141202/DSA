# Simplify Path

## Problem Statement
Given an absolute path to a file, simplify the path by removing any redundant directories (i.e., ".." and "."). The path is simplified by resolving the "." and ".." directories. For example, "/home/" is equivalent to "/home", and "/../" is equivalent to "/". Also, consider the edge cases where the input path is empty or contains only "/" or "." or "..". The function should return the simplified canonical path.

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates through each directory in the path, and if the directory is "..", it pops the last directory from the stack if the stack is not empty. If the directory is ".", it skips it. Otherwise, it pushes the directory into the stack. Finally, it constructs the simplified path from the directories in the stack.

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
        // Split the path by "/" and store the directories in a vector
        vector<string> dirs;
        string dir;
        for (char c : path) {
            if (c == '/') {
                if (!dir.empty()) {
                    dirs.push_back(dir);
                    dir.clear();
                }
            } else {
                dir += c;
            }
        }
        if (!dir.empty()) {
            dirs.push_back(dir);
        }

        // Use a stack to simplify the path
        stack<string> stack;
        for (string dir : dirs) {
            if (dir == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (dir != "." && !dir.empty()) {
                stack.push(dir);
            }
        }

        // Construct the simplified path from the stack
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
- Handle edge cases such as empty input path, or paths containing only "/" or "." or "..".
- Construct the simplified path from the directories in the stack.