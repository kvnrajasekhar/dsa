#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    float * area = (float *)malloc(sizeof(float)*n);
    int i,j;
    float p,temp;
    double s;
    for (i=0; i<n;i++) {
        p=(float)(tr[i].a+tr[i].b+tr[i].c)/2;
        s=(double)sqrt(p*(p-tr[i].a)*(p-tr[i].b)*(p-tr[i].c));
        area[i]=(float)s;
    }
    for(i=0;i<n-1;i++){
        for(j=0;j<n-i-1;j++){
            if(area[j]>area[j+1]){
                temp=area[j];
                area[j]=area[j+1];
                area[j+1]=temp;
                
                triangle t = tr[j];
                tr[j]=tr[j+1];
                tr[j+1]=t;
                
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
