class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildBST(arr):
    if len(arr) == 0:
        return None
    root = Node(arr[0])
    for i in range(1, len(arr)):
        cur = root
        while arr[i] < cur.data:
            if cur.left == None:
                temp = Node(arr[i])
                cur.left = temp
                break
            cur = cur.left
        while arr[i] > cur.data:
            if cur.right == None:
                temp = Node(arr[i])
                cur.right = temp
                break
            cur = cur.right
    return root
    
def printBST(root):
    if root == None:
        return
    printBST(root.left)
    print(root.data)
    printBST(root.right)
    
def weave(result, first, second, pre):
    if not first or not second:
        result.append(pre + first + second)
        return 
    else:
        firstHead, firstTail = first[0], first[1:]
        weave(result, firstTail, second, pre+[firstHead])
        
        secondHead, secondTail = second[0], second[1:]
        weave(result, first, secondTail, pre+[secondHead])

def printAll(root):
    if root is None:
        return []
    else:
        answer = []
        pre = [root.data]
        leftSeq = printAll(root.left) or [[]]
        rightSeq = printAll(root.right) or [[]]
        for i in range(len(leftSeq)):
            for j in range(len(rightSeq)):
                result = []
                weave(result, leftSeq[i], rightSeq[j], pre)
            answer += result
        return answer
    
if __name__ == '__main__':
    arr = [50, 60, 70, 20, 25, 10]
    root = buildBST(arr)
    print(printAll(root))
