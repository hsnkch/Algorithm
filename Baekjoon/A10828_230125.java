package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());

		Stack<Integer> st = new Stack<>();
		for (int i = 0; i < n; i++) {
			String order = br.readLine();
			String a[] = order.split(" ");
			if (order.contains("push")) {
				st.push(Integer.parseInt(a[1]));
			} else if (order.contains("size")) {
				sb.append(st.size()).append("\n");
			} else if (order.contains("empty")) {
				sb.append(st.empty() ? 1 : 0).append("\n");
			} else if (order.contains("top")) {
				if (st.empty()) {
					sb.append(-1).append("\n");
				} else {
					sb.append(st.peek()).append("\n");
				}
			} else if (order.contains("pop")) {
				if (st.empty()) {
					sb.append(-1).append("\n");
				} else
					sb.append(st.pop()).append("\n");
			}
		}
		System.out.print(sb);
	}
}