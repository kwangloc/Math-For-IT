#include<iostream>
#include<math.h>

using namespace std;
//perfect number

bool check_perfect_number(long k)
{
    long sum = 0;
    for (int i = 1; i < (k/2)+1; i++)
    {
    	if (k % i == 0)
            sum += i;
        if (sum > k)
            break;
	}

    if (sum == k)
        return true;
    else
        return false;
}

void list_perfect_number(long n)
{
    for (int i = 1; i < n+1; i++)
    {
    	if (check_perfect_number(i))
        	cout << i << " ";
	}
}

int main() {
	long n;
	cout << "Nhap so nguyen n: ";
	cin >> n;
    list_perfect_number(n);
}

