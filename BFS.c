/*Implementation of BFS traverasal mechanism*/
#include<stdio.h>
void BFS(int);//prototype declaration
int graph[10][10], visited[10],total;

main()
{
	inti,j;
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
	printf("\nBFS traversal is \n");
	BFS(0);//starting BFS with 0 vertex
}
void BFS(int vertex)
{
	int j;
	printf("%d\t",vertex);//printing visited vertex
	visited[vertex] = 1;// if vertex is visited then update queue 
	for(j=0;j<total;j++)
	{
		if(!visited[j] && graph[vertex][j] == 1 )
		{
			BFS(j);//recursively calling bfs for non visited vertices
		}
	}
}
