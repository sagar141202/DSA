# Simplify Path

## Problem Statement
Given an absolute path in a file system, simplify it by removing any redundant "." and ".." directories. The input path will always start with a "/" and will not end with a "/". The path will only consist of letters, numbers, ".", and "/". The function should return the simplified path. For example, "/home/" should become "/home", "/../" should become "/", and "/home//foo/" should become "/home/foo". The function should handle cases where the input path is empty or null.

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates over each directory in the path, and if the directory is not "." or "..", it pushes the directory onto the stack. If the directory is ".." and the stack is not empty, it pops the last directory off the stack. The simplified path is then constructed by popping all directories off the stack and concatenating them with "/" in between.

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
                if (directory != "") {
                    directories.push_back(directory);
                    directory = "";
                }
            } else {
                directory += c;
            }
        }
        if (directory != "") {
            directories.push_back(directory);
        }

        // Use a stack to keep track of the directories
        stack<string> stack;
        for (string dir : directories) {
            if (dir == "." || dir == "") {
                continue;
            } else if (dir == "..") {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else {
                stack.push(dir);
            }
        }

        // Construct the simplified path
        string simplifiedPath = "";
        vector<string> simplifiedDirectories;
        while (!stack.empty()) {
            simplifiedDirectories.push_back(stack.top());
            stack.pop();
        }
        for (int i = simplifiedDirectories.size() - 1; i >= 0; i--) {
            simplifiedPath += "/" + simplifiedDirectories[i];
        }
        if (simplifiedPath == "") {
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
Input: "/"
Output: "/"
```

## Key Takeaways
- Use a stack to keep track of the directories in the path.
- Handle the cases where the input path is empty or null.
- Use a vector to store the directories in the path and then use a stack to simplify the path.