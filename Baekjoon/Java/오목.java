import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int[][] boards = new int[19][19];
        for (int i = 0; i < 19; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 19; j++) {
                boards[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < 19; i++) {
            for (int j =0; j < 19; j++) {
                if (boards[i][j] != 0) {
                    BFS(i, j, boards);
                }
            }
        }
        System.out.println(0);

    }

    public static void BFS(int x, int y, int[][] boards) {
        int target = boards[x][y];
        int[] dx = {1, 0, 1, -1};
        int[] dy = {0, 1, 1, 1};

        for (int i = 0; i < 4; i++) {
            int cnt = 1;
            int rx = x + dx[i];
            int ry = y + dy[i];
            while (rx >= 0 && ry >= 0 && rx < 19 && ry < 19 && boards[rx][ry] == target) {
                cnt++;
                if (cnt == 5) {
                    if (0 <= x - dx[i] && x - dx[i] < 19 && 0 <= y - dy[i] && y - dy[i] < 19 && boards[x - dx[i]][y - dy[i]] == target) {
                        break;
                    }
                    if (0 <= rx + dx[i] && rx + dx[i] < 19 && 0 <= ry + dy[i] && ry + dy[i] < 19 && boards[rx + dx[i]][ry + dy[i]] == target) {
                        break;
                    }
                    System.out.println(target);
                    System.out.println((x + 1) + " " + (y + 1));
                    System.exit(0);
                }
                rx += dx[i];
                ry += dy[i];
            }
        }
    }
}