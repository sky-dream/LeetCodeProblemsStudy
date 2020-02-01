Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Example as below picture,In this tree, the lowest common ancestor of the nodes x and y is marked in dark green. Other common ancestors are shown in light green.

![Lowest_common_ancestor](Lowest_common_ancestor.svg.png)

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

![BinarySearchTree](binarysearchtree_improved.png)
 

# Example 1:
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```
# Example 2:
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

# Note:

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the BST.