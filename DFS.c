/*Implementation of DFS traverasal mechanism*/
#include<stdio.h>
#include<stdlib.h>

int graph[10][10], visited[10],total,arr[30];
static int k=0,count=0;
void DFS(int);
main()
{
	int i,j;
	printf("\nEnter the total number of vertices in graph\n");
	scanf("%d",&total);
	/*Adjacency matrix input*/
	printf("\nEnter the adjacency matrix\n");
	for(i=0;i<total;i++)
	{
		for(j=0;j<total;j++)
		{
			scanf("%d",&graph[i][j]);
		}
	}
	for(i=0;i<total;i++)
	{
		visited[i] = 0;
	}
	printf("\nDFS traversal is \n");
	DFS(0);
}
void DFS(int vertex)
{
	int j,c=0;
	count++;//increment count if 1 vertex is visited
	printf("%d\t",vertex);
	visited[vertex] = 1;//update stack for visited vertex
	for(j=0;j<total;j++)
	{
		if(!visited[j] && graph[vertex][j] == 1)
		{
			arr[++k] = j;//for non visited vertex push that vertex in array 
			c=1;
		}
		if(count == total)//base case for recursion(if all vertices are visited)
		{
			exit(0);
		}
	}
	if(c==1)//vertex not is visited and have other links
	{
		DFS(arr[k]);
	}
	else//vertex not is visited and don't have other links then go to previous vertex and go for other path which are not visited
	{
		k--;
		DFS(arr[k]);
	}	
}
