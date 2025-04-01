#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:

    def __init__(self, item):
        self.item = item
        self.next: [Node | None] = None


head: [Node | None] = None
curr: [Node | None] = None

def init():
    """ Викликається один раз на початку виконання програми. """
    global head, curr
    head = None
    curr = None


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return head is None



def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    global curr
    if empty() or curr.next is None:
        raise StopIteration
    curr = curr.next


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return curr.item



def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    global head, curr
    node = Node(item)
    if empty():
        head = curr = node
        return

    node.next = curr.next
    curr.next = node


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    global curr
    if empty():
        insert_after(item)
        return

    insert_after(curr.item)
    curr.item = item
    curr = curr.next


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    global head, curr
    if empty():
        return

    if curr is head:
        head = curr = curr.next
        return

    prev = head
    while prev.next is not curr:
        prev = prev.next

    prev.next = curr.next
    if curr.next is None:
        curr = prev
    else:
        curr = curr.next


def set_first():
    """Робить перший елемент списку поточним."""
    global curr, head
    curr = head

def set_last():
    """Робить останній елемент списку поточним."""
    global curr, head
    if head is None:
        return
    node = head
    while node.next:
        node = node.next
    curr = node

def prev():
    """Переміщує поточний елемент на попередній у списку."""
    global curr, head
    if curr is head:
        raise StopIteration

    prev_node = head
    while prev_node.next and prev_node.next != curr:
        prev_node = prev_node.next

    curr = prev_node  # Переміщення поточного елемента назад
