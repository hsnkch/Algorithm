package study;

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int a[] = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(a);
		int[] b = new int[n+1];
		for (int i = n-1; i >= 0; i-- ) {
			b[i] = (n-i)*a[i];
		}
		Arrays.sort(b);
		System.out.println(b[n]);
	}
}
