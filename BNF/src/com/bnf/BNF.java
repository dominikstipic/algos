package com.bnf;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class BNF {
	public static String PATH = "resources/cl.txt";
	
	public Map<String, List<String>> rules(){
		return null;
	}
	
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
	
	
	public static int randomChoice(int options) {
		double random = Math.random();
		for(int i = 1; i <= options; ++i) {
			double lower = (i-1)/options;
			double upper = (double) i/options;
			if(random >= lower & random < upper) {
				return i-1;
			}
		}
		return 0;
	}
	
	public static <T> T randomChoice(List<T> options) {
		int idx = randomChoice(options.size());
		return options.get(idx);
	}
	
	
	public static String generate(String start, Map<String, List<String>> rules) {
		List<String> expressions = rules.get(start);
		int idx = randomChoice(expressions.size());
		String expression = expressions.get(idx).strip();
		String[] tokens = expression.split(" ");
		String result = "";
		for(String token : tokens) {
			if(token.contains("<") && token.contains(">")) {
				if(VariableAssigner.isLeaf(token)) {
					List<String> options = VariableAssigner.getVariableOptions(token);
					String var = randomChoice(options);
					result += var + "";
				}
				else {
					String code = generate(token, rules);
					code = code.replaceAll("\"", "");
					result += code;
				}
			}
			else {
				result += token + "";
			}
		}
		return result;
	}
	
	public static void main(String[] args) throws IOException {
		Path p = Paths.get(PATH);
		List<String> strings = Files.readAllLines(p);
		Map<String, List<String>> bnfRules = new HashMap<>();
		
		for(String s : strings) {
			String[] parts = s.split("::=");
			String key = parts[0].strip();
			String[] expressions = parts[1].split("\\|");
			List<String> expressionList = Arrays.stream(expressions).map(t-> t.strip()).collect(Collectors.toList());
			bnfRules.put(key, expressionList);
		}
		
		String start = "<expression>";
		String code = generate(start, bnfRules);
		System.out.println(code);
	}
	

}
