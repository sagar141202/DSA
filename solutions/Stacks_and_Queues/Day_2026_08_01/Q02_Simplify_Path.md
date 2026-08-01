# Simplify Path

## Problem Statement
Given an absolute path to a file in a Unix-style file system, simplify the path by resolving the dot (.) and dot dot (..) notation. The input path is assumed to be valid and will not contain any whitespace or other special characters. For example, the path "/home/" should be simplified to "/home", and the path "/../" should be simplified to "/". The path "/home//foo/" should be simplified to "/home/foo".

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates over each directory in the path, and if the directory is "..", it pops the last directory from the stack if it is not empty. If the directory is not "." or "", it pushes the directory to the stack. Finally, it constructs the simplified path from the directories in the stack.

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
        for (string directory : directories) {
            if (directory == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (directory != "" && directory != ".") {
                stack.push(directory);
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
```

## Key Takeaways
- Use a stack to keep track of the directories in the path.
- Handle the dot (.) and dot dot (..) notation by popping the last directory from the stack if it is not empty.
- Construct the simplified path from the directories in the stack.