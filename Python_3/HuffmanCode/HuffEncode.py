################################################
#
#  Project 4    April 14, 2014
#  Huffman Codes
#
#  Alexander M. Thompson
#
#  File: HuffEncode.py
#
################################################
from arrayheap import ArrayHeap

def build_tree(heap): #Function to build the Huffman tree
    unique_ID = 200 #Number that indicates the internal leafs
    while len(heap) > 1:
        left = heap.pop() #Pops the left leaf
        right = heap.pop() #Pops the right leaf
        newcount = left[1]+right[1]
        branch = (unique_ID, newcount, left, right)
        heap.add(branch)
        unique_ID += 1 #adds one to make another internal leaf
    return heap.pop()

def preorder(tree, f, buff, sorter): #Function to make the preorder of the tree
    if tree != None:

        if int(tree[0]) > 199: #a conditonal for the internal leafs
            entry = "I:" + str(tree[0]) #prints the internal leafs
        else:
            entry = "L:" + str(tree[0]) #prints the leaves
           
            m = open("codetable.txt", 'w') #opens a file to be written into for the codetable
            code = (int(tree[0]), ''.join(buff))
            sorter.append(code)
            sorter = sorted(sorter)
            for code in sorter:
                code = str(code[0]) + " " + code[1]
                m.write(code)
                m.write('\n')
            m.close()

        f.write(entry)
        f.write('\n')
        left = tree[2]
        right = tree[3]

        if not left and not right:
            return

        buff.append('0')
        preorder(left, f, buff, sorter)
        buff.pop()

        buff.append('1')
        preorder(right, f, buff, sorter)
        buff.pop()

    if tree == None:
        print("abcdef")
        for code in sorter:
            m.write(code)
            m.write('\n')

def inorder(tree, k): #Function to make the inorder of the tree
    if tree != None:
        left = tree[2]
        right = tree[3]
        if int(tree[0]) > 199: 
            entry = "I:" + str(tree[0])
        else:
            entry = "L:" + str(tree[0])
        inorder(left, k)
        k.write(entry)
        k.write('\n')
        inorder(right, k)

def readFile(filename): #Reads the file and splits the data into two data points
    with open(filename, 'rt') as f:
        Occurrences = []
        for line in f:
            occurrence = line.split(' ')
            Occurrences.append((occurrence[0],int(occurrence[1]), None, None))
    return Occurrences

def updateHeap(heap, lyst): #Function to update the heap
    for item in lyst:
        heap.add(item)
    return heap

def readFile2(filename):
    with open(filename, 'rt') as f:
        characters = []
        for line in f:
            for c in line:
                characters.append(c)
    return characters

def even(filename):
    with open(filename, 'rt') as f:
        data = []
        for line in f:
            Data = line.split(' ')
            data.append(Data[1])
    return data

def compress(filename):
    new_file = open('HuffmanOutput.txt', 'w')
    for i in even(filename):
        new_file.write(str(i))
    new_file.close()
    

def main():
    Occurrences = readFile("counts.txt")
    compress('codetable.txt')
    Huff = ArrayHeap()
    Huff = updateHeap(Huff, Occurrences)
    HuffTree = build_tree(Huff)
    buff = []
    sorter = []
    with open("preorder.txt", 'w') as f:
        preorder(HuffTree, f, buff, sorter)
    with open("inorder.txt", 'w') as k:
        inorder(HuffTree, k)

main()
