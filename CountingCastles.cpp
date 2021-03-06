/*
Written by: Jay Lim
Start Date: Oct 7, 2016(lets see when I finally finish this one) LULZ
problem statement can be found here: https://projecteuler.net/problem=502
Note: works for 4x2, 3x3, 2x4. 
	- Tried to test for 13x10 but execution time is > 3 hrs....(stopped code at 300 million)
	- search for algorithm involving SUM(width!)
*/
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

class Board{

	int w, h;
	int aBoard[2][4];
	//int *aBoard = new int[w][h];

public:
	long long unsigned int count=0; //maximize the different castle's that can be formed
	Board(int x, int y): w(x>0 ? x:0), h(y>0 ? y:0), count(0)
	{
		//int aBoard [w][h];
		for(int i =0; i < x; i++) //width
		{
			for(int j =0; j<y; j++) //height
			{
				if(j==0)
					aBoard[i][j]=1;
				else
					aBoard[i][j]=0;
			//	cout << "x: "<< i << " y: " << j << "\t"<< aBoard[i][j] << endl;
			}
		}
	}

	void recurse(int x, int y, int numBlock)
	{
		//cout << count << endl;
		//cout << "x: " <<x << " y: "<< y<< endl;
		//if you reach the end of the Board(x)
		if(x >= w)
		{
			//cout << "if" <<endl;
			recurse(0, y+1, numBlock);
			return;
		}
		if(y >= h)
		{
			//cout << "if2" << endl;
			return;
		}
		aBoard[x][y] = 0;
	//	cout << "post if statements"<< endl;
		recurse(x+1,y,numBlock);
		if(x==0)
			numBlock++;
		else if(aBoard[x-1][y]==0)
			numBlock++;
		if(aBoard[x][y-1] != 0)
		{
		aBoard[x][y]=1;
	//	aBoard[x][y]=numBlock;
		if(numBlock%2 == 0)
			count++;
		recurse(x+1,y,numBlock);
		}	
	}
};

int main(int argc, char* argv[])
{	
	if(argc !=3)
	{
		cout <<"Enter dimensions of the board!" << endl;
	}
	else
	{
		int x = atoi(argv[1]);
		int y = atoi(argv[2]);
	
		Board b(x,y);
		
		if(y ==1)	//first level of board is just 1 big block
			return 1;
		//use a single recursive method. no forloops what so ever
		int start_s = clock();
		
		b.recurse(0, 1, 1);
		cout << "total count: "<<b.count << endl;
		int stop_s = clock();
		cout << "time: " << (stop_s - start_s)/double(CLOCKS_PER_SEC)*1000 <<endl;
	}
}


