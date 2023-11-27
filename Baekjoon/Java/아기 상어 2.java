import java.io.*;
import java.util.*;


public class Main {
    private static int ans;
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        ans = 0;
        Deque<int[]> q = new ArrayDeque<>();
        int[] dx = {1,1,1,0,0,-1,-1,-1};
        int[] dy = {1,0,-1,1,-1,1,0,-1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1){
                q.add(new int[]{i, j});
                }
            }
        }

        while (!q.isEmpty()) {
            int[] xy = q.pollFirst();
            for (int i = 0; i < 8; i++) {
                int x = xy[0] + dx[i];
                int y = xy[1] + dy[i];
                if (x >= 0 && x < n && y >= 0 && y < m) {
                    if (graph[x][y] == 0) {
                        q.add(new int[]{x, y});
                        graph[x][y] = graph[xy[0]][xy[1]] + 1;
                        ans = Math.max(ans, graph[xy[0]][xy[1]] + 1);
                    }
                }

            }
        }
        
        System.out.println(ans-1);
    }
}