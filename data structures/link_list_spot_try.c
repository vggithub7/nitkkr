#include <stdio.h>
#include<malloc.h>

struct node{
    int data;
    int *next;
};
struct node* create_new()
{
    struct node* head=NULL;
    return head;
}
struct node* create(struct node* head, int key){
    struct node* temp;
    temp=head;
    struct node* new_node=(struct node*)malloc(sizeof(struct node)) ;
    if(head==NULL){return new_node;}
    else
    {while(temp->next!=NULL)
        {temp=temp->next;}
    temp->next=new_node;
    new_node->data=key;
    
        return head;
        
    }
}
    void display(struct node* head)
    {   printf("%d->",head->data);
        while(head->next!=NULL){
            head=head->next;
            printf("%d->",head->data;);
        }
    }
    int main()
{
    int element;
    printf("Hello World");
    struct node* head=NULL;
    head=create_new();
    while(1){printf("\n enter elememnt: ");
        scanf("%d",&element);
        create(head,element);
        display(head);
    }
    return 0;
}
