#include <stdio.h>
#include <stdlib.h>
//declaring structure template
struct node
{
    int data; 
    struct node *right_child;
    struct node *left_child;
};
//function to create root node
struct node* new_node(int x)
{
    struct node *p;
    p = malloc(sizeof(struct node));
    p->data = x;
    p->left_child = NULL;
    p->right_child = NULL;
    return p;
}
//inserting given elements in tree
struct node* insert(struct node *root, int x)
{
    if(root==NULL)
        return new_node(x);
    else if(x>root->data) 
        root->right_child = insert(root->right_child,x);
    else
        root->left_child = insert(root->left_child,x);
    return root;
}
//searching an element is present in tree or not
struct node* search(struct node *root, int x)
{  //if element is found return root
    if(root==NULL || root->data==x)
        return root;
    else if(x>root->data) 
        return search(root->right_child, x);
    else
        return search(root->left_child,x);
}
//inserting a new element in tree
struct node *new_insert(struct node *root,int x,int r)
{
    int  ele;
    if(search(root,x)||x==r)
    { //if the given element is already present in tree,then BST rules breaks, so printing warning and asking another element
        printf("\n binary search tree won't allow duplicate elements!!!enter different elements!!!");
        printf("\n enter another element to insert:");
        scanf("%d",&ele);
        //inserting another element
        new_insert(root,ele,r);
    }
     else
    { // inserting new element into the tree
       if(root==NULL)
        {
            return new_node(x);
        }
        else if(x<root->left_child)//if element is less than root
        root->left_child=new_insert(root->left_child,x,r);
        else//if element is greater than root
        root->right_child=new_insert(root->right_child,x,r);
        return root;
    }
}
//finding inorder successor of right subtree
struct node* inorderrstree(struct node *root)
{
    if(root == NULL)
        return NULL;
    else if(root->left_child != NULL)
    //finding the  inorder successsot recursively
        return  inorderrstree(root->left_child); 
    return root;
}
//deleting an element from tree
struct node* delete(struct node *root, int x)
{
    if(root==NULL)
        return NULL;
    if (x>root->data)//if given element is greater than rootelement
        root->right_child = delete(root->right_child, x);
    else if(x<root->data)//if given element is lessthan rootelement
        root->left_child = delete(root->left_child, x);
    else//if given element is equal to root element
    {
        if(root->left_child==NULL && root->right_child==NULL)
        { //if element is leaf child
            free(root);
            return NULL;
        }
        else if(root->left_child==NULL || root->right_child==NULL)
        { //if the element have only one child
            struct node *temp;
            if(root->left_child==NULL)
                temp = root->right_child;
            else
                temp = root->left_child;
            free(root);
            return temp;
        }
        else//if the element have two children
        {  //finding right subtree inorder sucessor and assigning it to temp variable
            struct node *temp = inorderrstree(root->right_child);
            root->data = temp->data;
            //deleting given element and replacing the temp data
            root->right_child = delete(root->right_child, temp->data);
        }
    }
    return root;
}
//printing tree in inorder traversal
void inorder(struct node *root)
{
    if(root!=NULL) 
    {
        inorder(root->left_child); 
        printf(" %d ", root->data); 
        inorder(root->right_child); 
    }
}
//printing tree in preorder traversal
void preorder(struct node *root)
{
    if(root!=NULL)
    {
        printf(" %d ", root->data);
        preorder(root->left_child);
        preorder(root->right_child);
    }
}
//printing tree in postorder traversal
void postorder(struct node *root)
{
    if(root!=NULL)
    {
        postorder(root->left_child);
        postorder(root->right_child);
        printf(" %d ",root->data);
    }
}
//printing left view of tree
void leftviewprint(struct node *root,int level,int *height)
{
    if(root == NULL)
    {
        return;
    }
    if(*height < level)
    {
        printf("%d\t",root->data);
        *height = level;
    }
    //recursively getting the left view of BST
    leftviewprint(root->left_child,level+1,height);
    leftviewprint(root->right_child,level+1,height);
}
void leftview(struct node *root)
{
    int height= 0; 
    if(root == NULL){
        return;
    }
    else{
        leftviewprint(root,1,&height);
    }
}
//printing right view of tree
void rightviewprint(struct node *root,int level,int *height)
{
    if(root == NULL){
        return;
    }

    if(*height < level){
        printf("%d\t",root->data);
        *height = level;
    }
    //recursively getting the right view of BST
    rightviewprint(root->right_child,level+1,height);
    rightviewprint(root->left_child,level+1,height);
}
void rightview(struct node *root)
{
    int height = 0;
    if(root == NULL){
        return;
    }
    else{
        rightviewprint(root,1,&height);
    }
}
//main function
int main()
{
int ch/*for storing choice*/;
int i,r/*for storing root*/,n,x,bst[50]/*for storing elements*/;
struct node *root;
//for  printing main menu
printf("\n ** main menu** \n");
printf("\n 1.create and insert the input given:");
printf("\n 2.inorder traversal");
printf("\n 3.preorder traversal");
printf("\n 4.postorder traversal");
printf("\n 5.search an element");
printf("\n 6.delete an element");
printf("\n 7.insert a new element");
printf("\n 8.left view of tree");
printf("\n 9.right view of tree");
printf("\n enter your choice:");
scanf("%d",&ch);
    do
    {
        switch(ch)
        {
        case 1:
            printf("\nenter how many elements you want in tree with out root:");
            scanf("%d",&n);
            printf("\n enter the value that you want as ROOT:");
            scanf("%d",&r);
            root = new_node(r);
            for(i=1;i<=n;i++)
            {
                printf("\n enter bst[%d] val:",i);
                scanf("%d",&bst[i]);
            if(search(root,bst[i])||bst[i]==r)
            {
                printf("\n binary search tree won't allow duplicate elements!!!enter different elements!!!");
                printf("\n enter different element for bst[%d]:",i);
                scanf("%d",&x);
                insert(root,x);
            }
                insert(root,bst[i]);
            }
                break;
        case 2:
                printf("\n in inorder is:\n");
                inorder(root);
                break;
        case 3:
                printf("\n In preorder is:\n");
                preorder(root);
                break;
        case 4:
                printf("\n In postorder is:\n");
                postorder(root);
                break;
        case 5:
                printf("\n enter element to search:");
                scanf("%d",&x);
                if(search(root,x))
                    printf("\n %d is present in tree",x);
                else
                    printf("\n %d is not present in tree",x);
                break;
        case 6:
                printf("\n enter element to delete:");
                scanf("%d",&x);
                if(search(root,x))//searching if element is present in tree or not 
                {
                    delete(root,x);
                printf("\n %d is deleted from tree!!!",x);
                }
                else
                { //if given element is not present in tree, then printing message...
                    printf("\n the element you choosed is unable to delete, cause it is not present in tree, enter another element ");
                     //if given element is not in the tree ,re-entering another element to delete
                    printf("\n enter element to delete:");
                    scanf("%d",&x);
                    delete(root,x);
                }
                    break;
        case 7:
                    printf("\n enter element to insert:");
                    scanf("%d",&x);
                    new_insert(root,x,r);
                    break;
        case 8: 
                    printf("\n in left view the tree is..");
                    leftview(root);
                    break;
        case 9:
                    printf("\n in right view the tree is..");
                    rightview(root);
                    break;
        }
printf("\n enter your choice:");
scanf("%d",&ch);
    }while(ch<=9);//exit if choice exceeds 9
}
