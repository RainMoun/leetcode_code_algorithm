class LNode:
    def __init__(self, x):
        self.value = x
        self.next = None


# 方法一：就地修改链表(时间复杂度：O(n) 空间复杂度：O(1))
def reverse_order(head):
    node_pre = head  # 前驱结点
    node_now = head.next  # 当前结点
    node_next = node_now.next  # 后继结点
    while node_next:
        if node_now != head.next:
            node_now.next = node_pre
        else:
            node_now.next = None
        node_pre = node_now
        node_now = node_next
        node_next = node_next.next
    node_now.next = node_pre
    head.next = node_now
    return head


# 方法二：递归法(时间复杂度：O(n) 空间复杂度：O(1)) 性能有所下降
def reverse_recursive(head):
    if not head or not head.next:
        return head
    else:
        new_head = reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


def recursive_main(head):
    if not head or not head.next:
        return
    else:
        first_node = head.next
        new_head = reverse_recursive(first_node)
        head.next = new_head
        return new_head


# 方法三：插入法
def insert_reverse(head):
    if not head or not head.next:
        return None
    else:
        cur = head.next.next
        head.next.next = None
        while cur:
            next_node = cur.next
            cur.next = head.next
            head.next = cur
            cur = next_node
        return head


# 引申 单链表的逆序输出
def reverse_print(head):
    if not head:
        return
    else:
        reverse_print(head.next)
        print(head.value)


if __name__ == '__main__':
    node_head = LNode(None)
    node_1 = LNode(1)
    node_2 = LNode(2)
    node_3 = LNode(3)
    node_4 = LNode(4)
    node_5 = LNode(5)
    node_head.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_11 = node_head.next
    '''while node_11:
        print(node_11.value)
        node_11 = node_11.next
    node_12 = insert_reverse(node_head).next
    while node_12:
        print(node_12.value)
        node_12 = node_12.next'''
    reverse_print(node_head.next)
