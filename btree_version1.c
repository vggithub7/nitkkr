#include<stdio.h>
#include<conio.h>
#define TT 5

typedef struct b_tree{
	int keys[9];
	struct b_tree *ptr_array[10];
	//_Bool leaf;
	int leaf;
	int n;
}sbt;

sbt *create(sbt *root)
{
	sbt *temp;
	temp=(sbt*)malloc(sizeof(sbt));
	temp->leaf=1;
	temp->n=0;
	//root=NULL;
	return temp;
		
}
void splitroot(sbt **root){
	//checkifleaf
	//checkifnonleaf
	int i,T,mid_element;
	sbt *root1=*root;
	int temp=root1->n;
	sbt *newroot;
	newroot=NULL;
	newroot=create(newroot);
	T=((temp+1)/2)-1;//T=4
	sbt* rightnode=NULL;
	rightnode=create(rightnode);
	if(root1->leaf)
	{
		
		for(i=0;i<=T-1;i++){rightnode->keys[i]=root1->keys[T+1+i];	}
		root1->n=rightnode->n=T;
		mid_element=root1->keys[T];
		newroot->keys[0]=mid_element;
		newroot->ptr_array[0]=root1;
		newroot->ptr_array[1]=rightnode;
		newroot->leaf=0;
		(newroot->n)++;
		*root=newroot;
		//return newroot;
		printf("\nnewroot[0]:%d\n",newroot->keys[0]);
	}
	else if (!(root1->leaf)){
		for(i=0;i<=T-1;i++){rightnode->keys[i]=root1->keys[T+1+i];
							rightnode->ptr_array[i]=root1->ptr_array[T+i+1];	}//ptr_copied
							rightnode->ptr_array[i]=root1->ptr_array[2*T+1];//ptr_copied
		root1->n=rightnode->n=T;
		mid_element=root1->keys[T];
		newroot->keys[0]=mid_element;
		newroot->ptr_array[0]=root1;
		newroot->ptr_array[1]=rightnode;
		(newroot->n)++;
		*root=newroot;
		//return newroot;
	}
	//non leaf	non leaf	non leaf	non leaf	non leaf	non leaf	non leaf	
	
	//sbt *rooot;
	//sbt *newnode=create(rooot) 
}
void split_normal(sbt* root,int i){
	sbt* rightnode;int j;int T;
	T=4;
	rightnode=NULL;
	rightnode=create(rightnode);
	rightnode->leaf=root->ptr_array[i]->leaf;
	if(!(root->ptr_array[i]->leaf)){
					printf("entered_normal_split_nonleaf");
					for(j=0;j<=T-1;j++){rightnode->keys[j]=root->ptr_array[i]->keys[T+1+j];
									rightnode->ptr_array[j]=root->ptr_array[i]->ptr_array[T+1+j];		}
									rightnode->ptr_array[j]=root->ptr_array[i]->ptr_array[2*T+1];//ptr_copied
									rightnode->n=root->ptr_array[i]->n=T;
					for(j=(root->n);j>i;j--){
						root->keys[j]=root->keys[j-1];
						root->ptr_array[j+1]=root->ptr_array[j];
					}	
					root->ptr_array[j+1]=rightnode;
					root->keys[j]=root->ptr_array[i]->keys[T];
					(root->n)++;		
	}
	else{			printf("entered_normal_split_else_case(leaf)");
					for(j=0;j<=T-1;j++){rightnode->keys[j]=root->ptr_array[i]->keys[T+1+j];
							//rightnode->ptr_array[j]=root->ptr_array[i]->ptr_array[T+1+j];	
								}
							//rightnode->ptr_array[j]=root->keys[2*T+1];//ptr_copied
							rightnode->n=root->ptr_array[i]->n=T;
					for(j=(root->n);j>i;j--){
						root->keys[j]=root->keys[j-1];
						root->ptr_array[j+1]=root->ptr_array[j+0];
					}	
					root->ptr_array[j+1]=rightnode;
					root->keys[j]=root->ptr_array[i]->keys[T];
					(root->n)++;
	}
	
}

void insert_non_full(sbt *root,int data){
	int temp=root->n;
	printf("\nentered_insert_non_full");
	printf("root->keys[0]:%d",root->keys[0]);
	if (temp==0){root->keys[0]=data;}
	else{
	
	while(temp>0&&data<root->keys[temp-1]){
		
		root->keys[temp]=root->keys[temp-1];
		temp--;
	}
	root->keys[temp]=data;
	}
	(root->n)++;
	printf("\nroot->n %d ",root->n);
}
void insert(sbt **root,int data) 
{
	int i=0;
	//(*root)->n
	//check if FULL________splitcall()
	//CHECK IF LEAF________done!!!!!
	//NOW INSERT
	
	if ((*root)->n==9){printf("it is full_call split f on root \n");
					splitroot(root);insert(root,data);}
	//void splitroot(root);
		//printf(ëntering)
	else if((*root)->leaf==1){
		insert_non_full(*root,data);
	}
	else if((*root)->leaf==0){
	
		printf("\nentered last of all else if non leaf insertion");
		while(i<((*root)->n)	&&	data>((*root)->keys[i]	))
			{i++;			}
			//check_full_child_node
			if((*root)->ptr_array[i]->n==9){split_normal((*root),i);insert(root,data);	}
			else{
			printf("\ni:%d\n",i);
			insert(	&((*root)->ptr_array[i]),data	);	}
	}
	else
	{printf("entered last of all ");
	}
	
}



void main(){
	int i,value,j;
	sbt *root=NULL;
	root=create(root);
	printf("root->leaf %d",root->leaf);
	while(1){
	printf("\nenter::");
	scanf("%d",&value);
	insert(&root,value);
	printf("\n");
	for(i=0;i<root->n;i++){printf("rootdata[%d]=%d\n",i,root->keys[i]);}
	if(!(root->leaf))
	{for(j=0;j<=root->n;j++){
	printf("\nroot[%d]_child\n",j);
			for(i=0;i<root->ptr_array[j]->n;i++){printf("rootdata[%d]=%d\n",i,root->ptr_array[j]->keys[i]);}	
			printf("\n\n");
			//for(i=0;i<root->ptr_array[1]->n;i++){printf("rootdata[%d]=%d\n",i,root->ptr_array[1]->keys[i]);}
		}
	}
	printf("\n****************************************************");
}
}
/*
sbt insert(sbt *root,int datavg){
	
}
*/

/*

*/

/*

*/
