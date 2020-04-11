// leetcode time     cost : 108 ms
// leetcode memory   cost : 199.2 MB 
#include <vector>
#include <stdlib.h>
#include <string>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(Node* root) {
        string s;
        if (!root) {
            s = "#";
            return s;
        }
        s = to_string(root->val) + " " + to_string(root->children.size()); 
        for (const auto &child : root->children) {
            s = s + " " + serialize(child);
        }
        return s;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        istringstream is(data);
        return DFS(is);
    }

    Node* DFS(istringstream &is) {
        string s, size;
        is >> s;
        if (s == "#") return nullptr;
        is >> size;
        Node *p = new Node(stoi(s));
        for (int i = 0; i < stoi(size); ++i) {
            p->children.push_back(DFS(is));
        }
        return p;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));