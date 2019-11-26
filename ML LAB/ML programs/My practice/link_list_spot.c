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
    
    struct node* new_node=(struct node*)malloc(sizeof(struct node)) ;
    temp=head;
    new_node->data=key;
    new_node->next=NULL;
	if(head==NULL){new_node->data=key;
    new_node->next=NULL;
	return new_node;
	}
	
    else
    {
	while(temp->next!=NULL)
        {
		temp=temp->next;
		}
    
	temp->next=new_node;
    
       
        
    }
 return head;
}
    void display(struct node* head)
    {   
    	struct node* temp=NULL;
    	int i=0;
    	if(head->next!=NULL)
		{
		printf("%d",head->data);
		}
		else
		{
		printf("%d->",head->data);
		}
    	//getch();
    	//printf("chechk");
    	temp=head;
        
		while(temp->next!=NULL){
        	//printf("in while %d\n",i);
        	i=i+1;
			        	
            temp=temp->next;
            if(temp->next=NULL)
            {printf("%d",temp->data);
			}
			else{
			printf("%d->",temp->data);}
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
        head=create(head,element);
        display(head);
    }
    return 0;
}
