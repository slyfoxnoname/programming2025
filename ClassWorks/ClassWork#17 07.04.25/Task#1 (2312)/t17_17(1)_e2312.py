class searchTree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


    def insert(self, key):
        node = self # поточний вузол
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = searchTree(key)
                else:
                    node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = searchTree(key)
                    break
                else:
                    node = node.right
            else:
                break


    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()



    def height(self):
        stack = [(self, 1)]
        max_height = 0
        while stack:
            node, height = stack.pop()
            if height > max_height:
                max_height = height
            if node.left is not None:
                stack.append((node.left, height + 1))
            if node.right is not None:
                stack.append((node.right, height + 1))

        return max_height

if __name__ == '__main__':
    lst = [int(x) for x in input().split()]
    if lst[0] != 0:
        tree = searchTree(lst[0])
        for i in range(1, len(lst) - 1):
            if lst[i] == 0:
                break
            tree.insert(lst[i])
    print(tree.height())