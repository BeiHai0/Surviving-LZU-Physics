#include<stdio.h>
#include<math.h>

int main(){
	
	// 改进后的方法 
	
	float I[21];
	int i;
	
	I[20] = 1.0/2.0 * (1.0/(6*21)+1.0/(5*21)); // 放缩法后取平均估算I[20] 
	
	for(i=19; i>=0; i--){
		I[i] = (1.0/(i+1) - I[i+1] ) / 5.0; 
	}  
	
	for(i=0; i<=20; i++){
		printf("I%d的值为:%f\n",i,I[i]);
	}
	
	printf("ln1.2的值为:%f",log(1.2));
	
/*

未改进的方法 

float I[21];
int i;

	I[0] = log(1.2);

	for(i=1;i<=20;i++){
		I[i] = -5*I[i-1] + 1.0/i;
		printf("%f\n",I[i]);
}

*/

	return 0;
}



