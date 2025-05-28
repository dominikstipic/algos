package com.bnf;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class VariableAssigner {
	
	public static Map<String, List<String>> maps = Map.of(
			"<var>", getVars(),
			"<num_12>", getNums(12), 
			"<num_60>", getNums(59),
			"<num_24>", getNums(23)
			);
	
	public static List<String> getVars(){
		List<String> chars = new ArrayList<>();
		for(int c = 'a'; c < 'z'; ++c) {
			chars.add(String.valueOf(c));
		}
		for(int c = 0; c < 9; ++c) {
			chars.add(String.valueOf(c));
		}
		return chars;
	}
	
	public static List<String> getNums(int limit){
		List<String> xs = new LinkedList<>();
		for(int i = 0; i <= limit; ++i) {
			xs.add(String.valueOf(i));
		}
		return xs;
	}
	
	public static List<String> getVariableOptions(String c){
		return maps.get(c);
	}
	
	public static boolean isLeaf(String key) {
		return maps.keySet().contains(key);
	}

	public static void main(String[] args) {
		System.out.println(isLeaf("<var>"));
	}
}
