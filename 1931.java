package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		InputStreamReader reader = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(reader);
        
        int n = Integer.parseInt(br.readLine());
        int [][] a = new int [n][2];
        
        for (int i = 0; i < n; i++) {
        	String b = br.readLine();
        	String[] c = b.split(" ");
			a[i][0] = Integer.parseInt(c[0]);
			a[i][1] = Integer.parseInt(c[1]);
		}
        
        Arrays.sort(a, new Comparator<int[]>() {
        	public int compare(int[] o1, int[] o2) {
        		if(o1[1]==o2[1]) {
        			return o1[0]-o2[0];
        		} else {
        			return o1[1]-o2[1];
        		}
        	}
        });
        int min=0;
        int count=0;
        
        for (int i = 0; i < n; i++) {
			if(min<=a[i][0]) {
				min = a[i][1];
				count+=1;
			}
		}
        
        StringBuilder sb = new StringBuilder();
        sb.append(count);
        System.out.println(sb);
	}
}