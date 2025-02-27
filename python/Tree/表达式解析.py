import BinaryTree
#由于Tree和Stack在不同目录下，调用Stack要将Stack的路径添加到sys.path中
import sys
sys.path.append(r'python\Stack')
from Stack import Stack
#利用树结构解析表达式
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pstack = Stack
    etree = BinaryTree('')
    pstack.push(etree)
    currentTree = etree
    for i in fplist:
        if i == '(': #左括号入栈建左子树下降
            currentTree.insertLeft('')
            pstack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']: #数字设置节点并上升
            currentTree.setRootVal(int(i))
            parent = pstack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']: #运算符设置节点并下降
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pstack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':#右括号将树出栈
            currentTree = pstack.pop()
        else:
            raise ValueError('Invalid Input')
    return etree

