#include<stdio.h>
#include<conio.h>
#include<malloc.h>
struct node {
	
	int data ;
	int visit;
	struct node *next;
};



void  main(){
	
	int i=0,j,myval,n_O_vert=5;
	struct node *graph[20];
	struct node *new_node12;struct node *new_node15;struct node *new_node21;struct node *new_node25;struct node *new_node23;struct node *new_node24;struct node *new_node32;struct node *new_node34;struct node *new_node42;struct node *new_node45;struct node *new_node43;struct node *new_node54;struct node *new_node51;struct node *new_node52;
	new_node12=(struct node*)malloc(sizeof(struct node));
	new_node15=(struct node*)malloc(sizeof(struct node));
	new_node21=(struct node*)malloc(sizeof(struct node));
	new_node25=(struct node*)malloc(sizeof(struct node));
	new_node23=(struct node*)malloc(sizeof(struct node));
	new_node24=(struct node*)malloc(sizeof(struct node));
	new_node32=(struct node*)malloc(sizeof(struct node));
	new_node34=(struct node*)malloc(sizeof(struct node));
	new_node42=(struct node*)malloc(sizeof(struct node));
	new_node45=(struct node*)malloc(sizeof(struct node));
	new_node43=(struct node*)malloc(sizeof(struct node));
	new_node54=(struct node*)malloc(sizeof(struct node));
	new_node51=(struct node*)malloc(sizeof(struct node));
	new_node52=(struct node*)malloc(sizeof(struct node));

	new_node12->data=2;
	new_node12->next=NULL;
	new_node15->data=5;
	new_node15->next=NULL;
	new_node21->data=1;
	new_node21->next=NULL;
	new_node25->data=5;
	new_node25->next=NULL;
	new_node23->data=3;
	new_node23->next=NULL;
	new_node24->data=4;
	new_node24->next=NULL;
	new_node32->data=2;
	new_node32->next=NULL;
	new_node34->data=4;
	new_node34->next=NULL;
	new_node42->data=2;
	new_node42->next=NULL;
	new_node45->data=5;
	new_node45->next=NULL;
	new_node43->data=3;
	new_node43->next=NULL;
	new_node54->data=4;
	new_node54->next=NULL;
	new_node51->data=1;
	new_node51->next=NULL;
	new_node52->data=2;
	new_node52->next=NULL;

	/*for(i=1;i<=5;i++){

	graph[i]->data=i;
	//graph[i]->visit=0;
	graph[i]->next=NULL;
					}
	graph[1]->next=new_node1;
	//new_node1->data=2;
	*/
	graph[1]=new_node12;
	graph[2]=new_node21;
	graph[3]=new_node32;
	graph[4]=new_node42;
	graph[5]=new_node54;
	//graph[6]=new_node8;

	new_node12->next=new_node15;
	new_node21->next=new_node25;
	new_node25->next=new_node23;
	new_node23->next=new_node24;
	new_node32->next=new_node34;
	new_node42->next=new_node45;
	new_node45->next=new_node43;
	new_node54->next=new_node51;
	new_node51->next=new_node52;
printf("kuch bhi");
getch();

	for(i=1;i<=n_O_vert;i++){

	if(graph[i]!=NULL)//if not null then put null in both the vertices
	{
		myval=graph[i]->data;
		printf("2 vertices are **********  %d    and    %d    \n",i,graph[i]->data);
		graph[i]=NULL;
        printf("kuch bhi");
        getch();
		for(j=i+1;j<=5;j++)
		{	if(graph[j]->data==myval)
				{graph[j]=NULL;}
		}

		i++;
	}
	else if(graph[i]==NULL){if(i==n_O_vert)
                                {printf("reached end of vetices");}
                                    else{continue;}
	}



}

}
