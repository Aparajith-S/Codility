int solution(int H[], int N) 
{

int *stack = (int*)malloc(sizeof(int)*N);
int top=-1;
int count =0;
for(int i=0;i<N;i++)
{
 while(top>=0 && stack[top]>H[i])
  {top--;}
   if(top>=0&&stack[top]==H[i])
    {
    continue;
    }
    else
    {
      stack[++top]=H[i];
      count++;
     }
   }   
  return count;   
}
    
