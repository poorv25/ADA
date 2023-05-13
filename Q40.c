#include <stdio.h>
#include <stdlib.h>

/* Linked list node */
struct Node {
    int data;
    struct Node* next;
};

/* Function to merge two sorted linked lists */
struct Node* merge(struct Node* l1, struct Node* l2) {
    if (l1 == NULL) {
        return l2;
    }
    if (l2 == NULL) {
        return l1;
    }
    if (l1->data <= l2->data) {
        l1->next = merge(l1->next, l2);
        return l1;
    } else {
        l2->next = merge(l1, l2->next);
        return l2;
    }
}

/* Function to divide a linked list into two halves */
void split(struct Node* head, struct Node** first, struct Node** second) {
    struct Node* slow = head;
    struct Node* fast = head->next;

    while (fast != NULL) {
        fast = fast->next;
        if (fast != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
    }

    *first = head;
    *second = slow->next;
    slow->next = NULL;
}

/* Function to sort a linked list using merge sort */
void mergeSort(struct Node** headRef) {
    struct Node* head = *headRef;
    struct Node* first;
    struct Node* second;

    if (head == NULL || head->next == NULL) {
        return;
    }

    split(head, &first, &second);

    mergeSort(&first);
    mergeSort(&second);

    *headRef = merge(first, second);
}

/* Function to insert a node at the beginning of a linked list */
void insertAtBeginning(struct Node** headRef, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *headRef;
    *headRef = newNode;
}

/* Function to print the elements of a linked list */
void printList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    struct Node* head = NULL;
    insertAtBeginning(&head, 6);
    insertAtBeginning(&head, 3);
    insertAtBeginning(&head, 8);
    insertAtBeginning(&head, 4);
    insertAtBeginning(&head, 1);
    insertAtBeginning(&head, 9);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 5);
    printf("Original list:\n");
    printList(head);
    mergeSort(&head);
    printf("Sorted list:\n");
    printList(head);
    return 0;
}
