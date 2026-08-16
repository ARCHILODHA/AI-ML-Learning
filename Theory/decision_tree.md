# Decision Tree

## Definition

A Decision Tree is a supervised machine learning algorithm used for both classification and regression.

It makes decisions using a tree-like structure.

---

## Structure

A decision tree contains:

- Root Node
- Decision Nodes
- Branches
- Leaf Nodes

Example:

```text
           Age > 30?
           /       \
         Yes        No
         /           \
    Income > 50K?    No
      /      \
    Yes       No
    /          \
  Buy         Don't Buy
