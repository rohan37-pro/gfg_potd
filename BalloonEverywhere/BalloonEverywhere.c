#include <stdio.h>


int maxInstance(char s[]){
	struct structure
	{	
		int b;
		int a;
		int l;
		int o;
		int n;
		
	} balloon ;

	balloon.a = 0;
	balloon.b = 0;
	balloon.l = 0;
	balloon.o = 0;
	balloon.n = 0;

	int i = 0;
	while (s[i]){
		switch (s[i]){
			case 'b':
				balloon.b ++;
				break;
			case 'a':
				balloon.a ++;
				break;
			case 'l':
				balloon.l ++;
				break;
			case 'o':
				balloon.o ++;
				break;
			case 'n' :
				balloon.n ++;
				break;
		}
		i++;
	}

	balloon.l /= 2;
	balloon.o /= 2;
	
	int sort_lis[5] = {balloon.b, balloon.a, balloon.l, balloon.o, balloon.n};
	int smallest_num = sort_lis[0];
	for (int i=1; i<5; i++){
		if (smallest_num > sort_lis[i]){
			smallest_num = sort_lis[i];
		}
	}
	return smallest_num;

}


int main()
{
	char arr[10000];
	int len = 0;

	scanf("%s", arr);
	printf("%d\n",maxInstance(arr));
	return 0;
	
}