package asd;

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		long [] b = new long[n-1];
		long [] c = new long[n];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < n-1; i++) {
			b[i] = Long.parseLong(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			c[i] = Long.parseLong(st.nextToken());
		}	
		long d = c[0];
		long sum = 0;
		for (int i = 0; i < n-1 ; i++) {
			if(c[i]<d) {
				d = c[i];
			}
			sum += d*b[i];
		}
		System.out.println(sum);
	}	
}
