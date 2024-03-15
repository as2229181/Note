class Node:
    # """
    # An object for sorting a single node of a linked list
    # There are two attributes---data and the link to the next node in the list
    # """
    data=None
    next_node=None
    def __init__(self,data):
        self.data=data 
    def __repr__(self):
        return "<Node data:%s> " %self.data
    

class Linkedlist:
    def __init__(self):
        self.head=None    
    def is_empty(self):
        return self.head==None
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.next_node
        return count
    def add(self,data):
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def insert(self,data,index):
        if index==0:#如果資料是加在頭的話直接叫add來處理
            self.add(data)
        if index>0:
            new=Node(data)
            position=index
            current=self.head
        while position>1:
            current=Node.next_node
            position -=1
        prev_node=current
        next_node=current.next_node
        prev_node.next_node=new
        new.next_node=next_node
        return
    def remove(self,key):
        current=self.head
        previous=None#用來追蹤前一個資料
        found=False#a stop condition for a loop 用loop搜索linked list 當搜索到需要的資料的時候，便使用found = false來暫停loop
        while current and not found: #從LIST中尋找如果當current == none 代表一經搜索到tail且沒有符合得key,代表key不在linkedlist中
            if current.data==key and current==self.head:
                 found=True
                 self.head=current.next_node
            elif current.data==key:
                found=True
                previous.next_node=current.next_node
            else:#代表說key 的資料並沒有出現在linkedlist當中，所以重新指向 previous->current->current.next_node
                previous=current
                current=current.next_node
        return current
    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
        return None
    def __repr__(self):
        nodes=[]
        current=self.head
        while current:
            if current == self.head:
                nodes.append("[Head:%s]"%current.data)
            elif current.next_node is None:
                nodes.append('[Tail:%s]'%current.data)
            else:
                nodes.append('[%s]'%current.data)
            current=current.next_node
        return"->".join(nodes)