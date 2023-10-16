import java.io.*;
import java.util.*;


public class Main {
    static List<String> list = new ArrayList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String[][] boards = new String[5][5];
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                boards[i][j] = st.nextToken();
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                dfs(i, j, boards[i][j], boards, 0);
            }
        }
        System.out.println(list.size());
    }

    public static void dfs (int x, int y, String number, String[][] boards, int cnt) {
        if (cnt == 5){
            if (!list.contains(number)) {
                list.add(number);
            } return;
        }

        for (int i = 0; i < 4; i++) {
            int rx = x + dx[i];
            int ry = y + dy[i];
            if ((0 <= rx && rx < 5) && (0 <= ry && ry < 5)) {
                dfs(rx, ry, number + boards[rx][ry], boards, cnt + 1);
            }
        }
    }

}
