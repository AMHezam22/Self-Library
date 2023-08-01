bool sieve[1000000+1]={true};
void buildSieve(){
	ll lon = 1000000+1;
	for (int i = 2; i*i <= lon; ++i) {
		if(sieve[i]){
			for (int j = i*i; j<lon; j+=i) {
				sieve[j] = false;
			}
		}
		
	}
}