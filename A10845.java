package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());

		LinkedList<String> qu = new LinkedList<String>();
		for (int i = 0; i < n; i++) {
			String order = br.readLine();
			String a[] = order.split(" ");
			if (order.contains("push")) {
				qu.add(a[1]);
			} else if (order.contains("pop")) {
				if (qu.isEmpty()) {
					sb.append(-1).append("\n");
				} else
					sb.append(qu.poll()).append("\n");
			} else if (order.contains("size")) {
				sb.append(qu.size()).append("\n");
			} else if (order.contains("empty")) {
				sb.append(qu.isEmpty() ? 1 : 0).append("\n");
			} else if (order.contains("front")) {
				if (qu.isEmpty()) {
					sb.append(-1).append("\n");
				} else {
					sb.append(qu.peek()).append("\n");
				}
			} else if (order.contains("back")) {
				if (qu.isEmpty()) {
					sb.append(-1).append("\n");
				} else
					sb.append(qu.getLast()).append("\n");
			}
		}
		System.out.print(sb);
	}
}