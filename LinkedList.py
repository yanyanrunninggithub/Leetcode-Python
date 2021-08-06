#21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1==None and l2==None:
            return None
        if l1==None:
            return l2
        if l2==None:
            return l1
        p = l1
        q = l2
        res = None
        r = res
        if p.val <= q.val:
            res = p
            p = p.next
        else:
            res = q
            q = q.next
        r = res
        while p!=None and q!=None:
            if p.val <= q.val:
                r.next = p
                r = p
                p = p.next
            else:
                r.next = q
                r = q
                q = q.next
        if p==None and q!=None:
            r.next = q
        elif q==None and p!=None:
            r.next = p
        else:
            r.next =None
        return res
#203. Remove Linked List Elements
class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        while head!= None and head.val == val:
            head = head.next
        p = head
        pre = None
        #post = None
        flag = True
        head_res = None
        while p != None:
            #post = p.next
            if p.val == val:
                pre.next = p.next
                p = p.next
                continue   #if meet continuous same val, we should check the next p
            if flag:
                head_res = p
                flag = False
            pre = p
            p = p.next
        return head_res