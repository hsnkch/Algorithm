import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int r1 = Integer.parseInt(st.nextToken());
        int c1 = Integer.parseInt(st.nextToken());
        int r2 = Integer.parseInt(st.nextToken());
        int c2 = Integer.parseInt(st.nextToken());
        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = -1;
            }
        }
        System.out.println(BFS(r1,c1,n,r2,c2,graph));
    }

    public static int BFS(int r1, int c1, int n, int r2, int c2, int[][] graph) {
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{c1, r1});
        int[] dx = {-1, 1, -2, 2, -1, 1};
        int[] dy = {-2, -2, 0, 0, 2, 2};
        graph[c1][r1] = 0;
        while (!q.isEmpty()) {
            int[] cur = q.pollFirst();
            int x = cur[1];
            int y = cur[0];
            for (int i = 0; i < 6; i++) {
                int rx = x + dx[i];
                int ry = y + dy[i];
                if (0 <= rx && rx < n && 0 <= ry && ry < n && graph[ry][rx] == -1) {
                    graph[ry][rx] = graph[y][x] + 1;
                    q.offer(new int[]{ry, rx});
                }
            }
        }
        return graph[r2][c2];
    }
}
