#include<strings.h>
struct Results{
	int *A;
	int M; // Length of the Array
};

void record(char *S , int *A , char key, int index)
{
if(S[index] == key)
	A[index] = index;
else if (index !=0)
	A[index] = A[index-1];
else 
	A[index] = -1;
	
}

struct Results solution(char *S ,int P[] ,int Q[], int M)
{
	struct Results result;
	int N;
	result.A = (int*)malloc(sizeof(int)*M);
	result.M = M;
	N=strlen(S);
	int *genA = (int*)malloc(sizeof(int)*N);
	int *genC = (int*)malloc(sizeof(int)*N);
	int *genG = (int*)malloc(sizeof(int)*N);
	int *genT = (int*)malloc(sizeof(int)*N);
	
	for(int i=0;i<M;i++)
	{
		if(genA[Q[i]]>=P[i])
		{
			result.A[i] =1;
			continue;
		}
		else if(genC[Q[i]]>=P[i])
			{
			result.A[i] =2;
			continue;
		}
		else if(genG[Q[i]]>=P[i])
			{
			result.A[i] =3;
			continue;
		}
		else if(genT[Q[i]]>=P[i])
			{
			result.A[i] =4;
			continue;
		}
	}
return result;
}