# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving '..' and '.' in the path. The path is made up of a sequence of directories where each directory is represented as a string separated by '/'. The function should return the simplified path. For example, if the input is "/home/", the output should be "/home". If the input is "/../", the output should be "/". If the input is "/home//foo/", the output should be "/home/foo". The function should handle all edge cases such as consecutive '/' characters, empty strings, and paths that start or end with '/'.

## Approach
The algorithm uses a stack to keep track of the directories in the path. It iterates through each directory in the path, and if the directory is "..", it pops the last directory from the stack. If the directory is not "." or "", it pushes the directory onto the stack. Finally, it constructs the simplified path by joining the directories in the stack with "/".

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

class Solution {
public:
    string simplifyPath(string path) {
        // Split the path into directories
        stringstream ss(path);
        string directory;
        vector<string> directories;
        while (getline(ss, directory, '/')) {
            // Ignore empty strings and "."
            if (directory != "" && directory != ".") {
                directories.push_back(directory);
            }
        }

        // Use a stack to keep track of the directories
        vector<string> stack;
        for (string dir : directories) {
            // Handle ".."
            if (dir == "..") {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else {
                stack.push_back(dir);
            }
        }

        // Construct the simplified path
        string simplifiedPath = "/";
        for (string dir : stack) {
            simplifiedPath += dir + "/";
        }

        // Remove the trailing "/"
        if (simplifiedPath != "/") {
            simplifiedPath.pop_back();
        }

        return simplifiedPath;
    }
};

int main() {
    Solution solution;
    cout << solution.simplifyPath("/home/") << endl;  // Output: "/home"
    cout << solution.simplifyPath("/../") << endl;    // Output: "/"
    cout << solution.simplifyPath("/home//foo/") << endl;  // Output: "/home/foo"
    return 0;
}
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
- Handle ".." by popping the last directory from the stack.
- Ignore "." and empty strings.
- Construct the simplified path by joining the directories in the stack with "/".