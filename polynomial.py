class Node:
    def __init__(self,coeff,exp):
        self.coeff=coeff
        self.exp=exp
        self.next=None
class Polynomial:
    def __init__(self):
        self.head=None
       
    def insert(self,coeff,exp):
        new_node=Node(coeff,exp)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current:
            if current.exp==exp:
               current.coeff+=coeff
               return
            if current.next is None:
               break
            current=current.next
        current.next=new_node
    def delete(self,exp):
       current=self.head
       previous=None
       while current:
           if current.exp==exp:
               if previous is None:
                   self.head=current.next
               else:
                   previous.next=current.next
               return
           previous=current
           current=current.next
    def display(self):
        current=self.head
        terms=[]
        while current:
            if current.exp==0:
                terms.append(f'{current.coeff}')
            elif current.exp==1:
                terms.append(f'{current.coeff}x')
            else:
                terms.append(f'{current.coeff}x^{current.exp}')
            current=current.next
        print('+'.join(terms) if terms else '0')
    def merge(self,poly2):
        result=Polynomial()
        combined={}
        current=self.head
        while current:
            combined[current.exp]=combined.get(current.exp,0)+current.coeff
            current=current.next
        current=poly2.head
        while current:
            combined[current.exp]=combined.get(current.exp,0)+current.coeff
            current=current.next
        for exp in sorted(combined.keys(),reverse=True):
            result.insert(combined[exp],exp)
        return result

P1=Polynomial()
P1.insert(5,4)
P1.insert(3,2)
P1.insert(2,0)
P1.display()

P2=Polynomial()
P2.insert(4,4)
P2.insert(7,1)
P2.insert(8,0)
P2.display()
           
P3=P1.merge(P2)
P3.display()

P1.delete(2)
P1.display()
