#include<iostream>

void eratos(long n)
{
	for(int i = 2; i < n; i++)
	{
		if(i%2 != 0 && i%3 != 0)
		{
			std::cout << i << " ";
		}
	}
}

int main()
{
	long n;
	std::cin >> n;
	eratos(n);
	return 0;
}
