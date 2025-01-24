#include<stdio.h>
#include<math.h>
#include<time.h>

double p(double x){
	return 1.0 / (1+exp(x)) / log(2);
}

double f(double x){
	
	return x;
	
}

int main(){
	
	int i;
	int cnt = 0;
	
	double a[100001];
	int rand_int;
	double rand_double;
	
	double state_0 = 1.0;
	double state_1;
	double alpha;
	
	double p_i, p_j;
	
	double tmp;
	
	double integral = 0.0;
	
	srand(time(0));
	
	for(i=1; i<100001; i++){
		
		while(1){
		
			rand_int = rand()%1000;
			rand_double = rand_int/1000.0 ; //0~1
		
			state_1 = state_0+rand_double;
			
			//printf("%lf", state_1);
		
			p_j = p(state_1);
			p_i = p(state_0);
		
			if( p_j/p_i <= 1.0 ){
			
				alpha = p_j / p_i;
			
			}else{
			
				alpha = 1.0;
			
			}
		
			rand_int = rand()%1000;
			rand_double = rand_int/1000.0 ; // 0~1Ëæ»úÊý 

			tmp = rand_double;
			
			cnt++;
		
			if(tmp<=alpha){
			
				state_0 = state_1;
				
				//printf("%d\n", cnt);
			
			}
			
			if(cnt>=1000000){
	
				a[i] = state_0;
					
				break;
				
			}
		
		}
		
	}
	
	for(i=1; i<100001; i++){
		
		integral += f(a[i]);
		//printf("%lf", integral);
		
	}
	
	integral /= 100000;
	
	integral *= log(2);
	
	printf("%lf", integral);
	
	
	return 0;
}
