#include<iostream>
#include<math.h>
#include<vector>

using namespace std;

bool checkPrime(int n){
    if(n<2) return false;
    for(int i=2;i <=sqrt(n);i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

int main()
{
	vector<int> uocSNT;
	int n, tmp;
//	int arr[20] = {0};
	cout << "Nhap vao so nguyen n: ";
	cin >> n;
	tmp = n;
	cout << "\nCac uoc SNT cua n la: ";
	for (int i=2;i<=n;i++)
	{
		if(checkPrime(i)) 
		{
			uocSNT.push_back(i);
			cout << i << " ";
		}
	}
	
	cout << endl << n << "=";
	for (int i = 0; i < uocSNT.size(); i++)
	{
		int soMu = 0;
		while(tmp % uocSNT[i]== 0)
		{
//			arr[uocSNT[i]]++;
			soMu++;
			tmp /= uocSNT[i];
		}
		if (soMu != 0)
		{
			cout << uocSNT[i] << "^" << soMu << ".";
		}
	}
	

//	for(int i = 0; i < 20; i++)
//	{
//		
//		if(arr[i] != 0)
//		{
//			cout << i << "^" << arr[i] << ".";
//		}
//	}
	return 0;
}
