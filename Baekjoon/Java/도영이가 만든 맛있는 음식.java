import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] flavors;
    static int[][] arr;
    static int result = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        flavors = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            flavors[i][0] = Integer.parseInt(st.nextToken());
            flavors[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            arr = new int[i][2];
            DFS(0, 0);
        }

        System.out.println(result);
    }

    public static void DFS(int depth, int start) {
        if (depth == arr.length) {
            int sour = 1;
            int bitter = 0;
            for (int i = 0; i < arr.length; i++) {
                sour *= arr[i][0];
                bitter += arr[i][1];
            }
            if (Math.abs(sour - bitter) < result) {
                result = Math.abs(sour - bitter);
            }
            return;
        }
        for (int i = start; i < n; i++) {
            arr[depth] = flavors[i];
            DFS(depth + 1, i + 1);
        }

    }
}