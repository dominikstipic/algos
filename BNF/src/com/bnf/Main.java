package com.bnf;


public class Main {
	
	public static int randomChoice(int options) {
		double random = Math.random();
		double delta = 1 / options;
		for(int i = 1; i <= options; ++i) {
			double lower = (i-1)/options;
			double upper = (double) i/options;
			if(random >= lower & random < upper) {
				return i-1;
			}
		}
		return 0;
	}
	
	public static void main(String[] args) {
		int x = randomChoice(2);
		System.out.println(x);
		
	}

}
