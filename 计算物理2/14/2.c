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
	
	srand(time(0));
	
	int i;
	int cnt = 0;
	
	int rand_int;
	double rand_double;
	double sample;
	
	double state_0 = 0.0;
	double state_1;
	double alpha;
	
	double p_i, p_j;
	
	double tmp;
	
	double integral = 0.0;
	
	while(1){
		
			rand_int = rand();
			rand_double = rand_int ; // 随机数 
			
			//printf("%lf\n", rand_double);
		
			state_1 = rand_double;
		
			p_j = p(state_1);
			p_i = p(state_0);
		
			if( p_j/p_i <= 1.0 ){
			
				alpha = p_j / p_i;
			
			}else{
			
				alpha = 1.0;
			
			}
		
			rand_int = rand()%1000;
			rand_double = rand_int/1000.0 ; // 0~1随机数 
			//printf("%lf\n", rand_double);
			tmp = rand_double;
		
			cnt++;
			
			if(tmp<=alpha){
			
				state_0 = state_1;
			
				if(cnt>=1000000){
				
					sample = state_1;
					
					integral += sample;
					
					break;
				
				}
			}
	}
	
	for(i=1; i<10000001; i++){
		
		rand_int = rand();
			rand_double = rand_int ; // 随机数 
			
			//printf("%lf\n", rand_double);
		
			state_1 = rand_double;
		
			p_j = p(state_1);
			p_i = p(state_0);
				
				//printf("%d\n", cnt);
			
			}
		
		}
		
	}
	
	integral /= 10000000;
	
	integral *= log(2);
	
	printf("%lf", integral);
	
	
	return 0;
}
