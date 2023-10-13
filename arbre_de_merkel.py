import math
import hashlib


data = ['jfjfjfjfj','gfjh','fgjh','fjhfsf','sgfbb','sfgw','sgfgwg','sgfdg','ssss','2222']

class MerkleTreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        self.hashValue = hashlib.sha256(value.encode('utf-8')).hexdigest()
        
leafnodes = []
for i in range(len(data)):
    leafnodes.append(MerkleTreeNode(data[i]))

    
    
    
def TreeLevel(leafnodes):
    n=0
    new_nodes_list = []
    for i in range(int(len(leafnodes)/2)):
        k = MerkleTreeNode(leafnodes[n].value + leafnodes[n+1].value)
        k.left = leafnodes[n]
        k.right= leafnodes[n + 1]
        new_nodes_list.append(k)
        n += 2

    
    
        if n+1 >= len(data):
            break
        
    if(len(leafnodes)>n):
        new_nodes_list.append(leafnodes[n-2])
    
    return new_nodes_list


def merkel_root(data):
    if len(data)<=2:
        if len(data) == 1:
            return MerkleTreeNode(data[0])
        else:
            leafnodes = []
            for i in range(len(data)):
                leafnodes.append(MerkleTreeNode(data[i]))
            k = MerkleTreeNode(leafnodes[0].value + leafnodes[1].value)
            k.left = leafnodes[0]
            k.right= leafnodes[1]
            return k
    else:
        leafnodes = []
        for i in range(len(data)):
            leafnodes.append(MerkleTreeNode(data[i]))

        tree_level = leafnodes
        for i in range(int(math.log2(len(data))) + 1):
            tree_level = TreeLevel(tree_level)
        return tree_level[0]

    
print(merkel_root(data).hashValue)
print(merkel_root(['dddd']).hashValue)
print(merkel_root(['ddd','hello.friend']).hashValue)