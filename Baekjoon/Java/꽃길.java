import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int ans;
    private static int n;
    private static int total;
    private static int[] dx = {0, 0, 0, 1, -1};
    private static int[] dy = {1, -1, 0, 0, 0};
    private static int[][] price;
    private static int[][] visited;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        price = new int[n][n];
        visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                price[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ans = Integer.MAX_VALUE;
        total = 0;
        dfs(0);
        System.out.println(ans);
    }

    public static boolean check(int x, int y) {
        for (int i = 0; i < 5; i++) {
            int rx = x + dx[i];
            int ry = y + dy[i];
            if (visited[rx][ry] == 1) {
                return false;
            }
        }
        return true;
    }

    public static void dfs(int depth) {
        if (depth == 3) {
            ans = Math.min(ans, total);
            return;
        }

        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (check(i, j)) {
                    for (int k = 0; k < 5; k++) {
                        int ri = i + dx[k];
                        int rj = j + dy[k];
                        visited[ri][rj] = 1;
                        total += price[ri][rj];
                    }

                    dfs(depth + 1);

                    for (int k = 0; k < 5; k++) {
                        int ri = i + dx[k];
                        int rj = j + dy[k];
                        visited[ri][rj] = 0;
                        total -= price[ri][rj];
                    }
                }
            }
        }
    }
}