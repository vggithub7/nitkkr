#include<stdio.h>
#include<conio.h>

struct node {
	
	int data ;
	int visit;
	struct node *next;
};



void  main(){
	
	struct node *graph[20];
	struct node new_node1;struct node new_node2;struct node new_node3;struct node new_node4;struct node new_node5;struct node new_node6;struct node new_node7;struct node new_node8;
	new_node1=(struct node*)malloc(sizeof(struct node));
	new_node2=(struct node*)malloc(sizeof(struct node));
	new_node3=(struct node*)malloc(sizeof(struct node));
	new_node4=(struct node*)malloc(sizeof(struct node));
	new_node5=(struct node*)malloc(sizeof(struct node));
	new_node6=(struct node*)malloc(sizeof(struct node));
	new_node7=(struct node*)malloc(sizeof(struct node));
	new_node8=(struct node*)malloc(sizeof(struct node));
	new_node1->data=2;
	new_node1->next=NULL;
	new_node2->data=4;
	new_node2->next=NULL;
	new_node3->data=5;
	new_node3->next=NULL;
	new_node4->data=6;
	new_node4->next=NULL;
	new_node5->data=5;
	new_node5->next=NULL;
	new_node6->data=2;
	new_node6->next=NULL;
	new_node7->data=4;
	new_node7->next=NULL;
	new_node8->data=6;
	new_node8->next=NULL;
	
	
	/*for(i=1;i<=5;i++){
	
	graph[i]->data=i;
	//graph[i]->visit=0;
	graph[i]->next=NULL;
					}
	graph[1]->next=new_node1;
	//new_node1->data=2;
	*/
	graph[1]=new_node1;
	graph[2]=new_node3;
	graph[3]=new_node4;
	graph[4]=new_node6;
	graph[5]=new_node7;
	graph[6]=new_node8;
	
	new_node1->next=new_node2;
	//new_node2->next=NULL;
	//new_node3->next=NULL;
	new_node4->next=new_node5;
	//new_node5->next=NULL;
	//new_node6->next=NULL;
	//new_node7->next=NULL;
	//new_node8->next=NULL;
	graph[i]->next=NULL;
	graph[i]->next=NULL;
	graph[i]->next=NULL;
	graph[i]->next=NULL;
	while(graph[i]->next!=NULL)
	{
		myval=graph[i]->next->data;
		graph[i]->next=NULL;
		for(j=i+1;j<=6;j++)
		{	if(graph[j]->data=myval)
				{graph[j]->next=NULL;}
		}
		
		i++;
	}
	
						
	
}
