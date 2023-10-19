import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Deque<int []> q = new ArrayDeque<>();
        int[] balloons = new int[n];

        for (int i = 0; i < n; i++) {
            balloons[i] = Integer.parseInt(st.nextToken());
        }

        sb.append("1 ");
        int moves = balloons[0];
        for (int i = 1; i < n; i++) {
            q.add(new int[]{i + 1, balloons[i]});
        }

        while (!q.isEmpty()) {
            if (moves > 0) {
                for (int i = 1; i < moves; i++) {
                    q.add(q.poll());
                }
                int[] next = q.poll();
                moves = next[1];
                sb.append(next[0] + " ");
            } else {
                for (int i = 1; i < -moves; i++) {
                    q.addFirst(q.pollLast());
                }

                int[] next = q.pollLast();
                moves = next[1];
                sb.append(next[0] + " ");
            }

        }
        System.out.println(sb.toString());



    }
}