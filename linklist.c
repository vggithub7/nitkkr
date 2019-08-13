/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

struct node{
    int data;
    struct node *next;
    
};

struct node* create(){
    int n;
    struct node *start=NULL,*last=NULL,*new_node=NULL;
    printf("Enter the data");
    scanf("%d",&n);
    while(n!=-1)
    {
    new_node=(struct node*)malloc(sizeof(struct node));
    new_node->data=n;
    new_node->next=NULL;
        if (start==NULL)
        {
               start=last=new_node;
        }
            
        else
        {
            last->next=new_node;
            last=new_node;
        }
        printf("Enter the data");
    scanf("%d",&n);
    }
    return start;
}
void display(struct node* start)
{while (start->next!=NULL )
    {printf("%d->",start->data);
    start=start->next;}
    printf("%d",start->data);
}
int main()
{
    struct node *linlist;
    linlist=create();
    printf("\n");
    display(linlist);
    return 0;
}

