import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private int ans;
    static void bfs(Queue<int[]> q, char[][] board) {
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        while (!q.isEmpty()) {
            int[] point = q.poll();
            int x = point[0];
            int y = point[1];
            board[x][y] = '.';
            for (int i = 0; i < 4; i++) {
                int rx = x + dx[i];
                int ry = y + dy[i];
                if (rx >= 0 && rx < board.length && ry >= 0 && ry < board[0].length && board[rx][ry] == 'O') {
                    board[rx][ry] = '.';
                }
            }
        }
    }

    static void simulate(int t, Queue<int[]> q, char[][] board) {
        if (t == 1) {
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    if (board[i][j] == 'O') {
                        q.add(new int[]{i, j});
                    }
                }
            }
        } else if (t % 2 == 1) {
            bfs(q, board);
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    if (board[i][j] == 'O') {
                        q.add(new int[]{i, j});
                    }
                }
            }
        } else {
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    board[i][j] = 'O';
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        char[][] board = new char[r][c];

        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        Queue<int[]> q = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            simulate(i, q, board);
        }

        for (char[] row : board) {
            System.out.println(new String(row));
        }
    }
}