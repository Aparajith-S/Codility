#include<math.h>

long int solution(int N)
{
  int b = sqrt(N);
  while(N%b != 0)
  {
    b--;
  }
  int l = N/b;
  return (long int)(2*(l+b));
}
