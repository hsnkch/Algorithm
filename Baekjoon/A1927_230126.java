package study;

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> a = new PriorityQueue<>();
		
		for (int i = 0; i < n; i++) {
			int b = Integer.parseInt(br.readLine());
			if(b==0) {
				if(!a.isEmpty())	System.out.println(a.poll());
				else System.out.println(0);
			} else {
				a.add(b);
			}
		}
		
	}
}
