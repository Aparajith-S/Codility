int solution(int A[], int N)
{
	int count = 0;
	int *stack = (int*)malloc(N * sizeof(int));
	int top = -1;
	for (int i = 0; i < N; i++)
	{
		if (top != -1)
		{
			if (A[i] <= 0)
				if (abs(stack[top]) == abs(A[i]))
					continue;
				else
					stack[++top] = A[i];
			else if (A[i] > 0)
			{
				while (top != -1)
				{
					if (abs(stack[top]) <= abs(A[i]))
					{
						if (abs(stack[top]) < abs(A[i]))
							count += 1;
						top--;
					}
					else
						break;
				}
				stack[++top] = A[i];
			}
		}
		else
			stack[++top] = A[i];
	}
