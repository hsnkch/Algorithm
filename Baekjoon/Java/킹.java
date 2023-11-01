import java.io.*;
import java.util.*;

public class Main {
    static int x;
    static int y;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String king = st.nextToken();
        String stone = st.nextToken();
        int kingX = king.charAt(0) - 'A' + 1;
        int kingY = Integer.parseInt(king.substring(1));
        int stoneX = stone.charAt(0) - 'A' + 1;
        int stoneY = Integer.parseInt(stone.substring(1));
        int n = Integer.parseInt(st.nextToken());
        Map<String, int[]> moves = new HashMap<>(){{
            put("R", new int[]{1, 0});
            put("L", new int[]{-1, 0});
            put("T", new int[]{0, 1});
            put("B", new int[]{0, -1});
            put("RT", new int[]{1, 1});
            put("LT", new int[]{-1, 1});
            put("RB", new int[]{1, -1});
            put("LB", new int[]{-1, -1});
        }};

        for (int i = 0; i < n; i++) {
            String move = br.readLine();
            int dx = moves.get(move)[0];
            int dy = moves.get(move)[1];
            int nx = kingX + dx;
            int ny = kingY + dy;
            if (nx >= 1 && nx <= 8 && ny >= 1 && ny <= 8) {
                // 킹과 돌의 새로운 위치 계산
                if (nx == stoneX && ny == stoneY) {
                    int newStoneX = stoneX + dx;
                    int newStoneY = stoneY + dy;
                    if (newStoneX >= 1 && newStoneX <= 8 && newStoneY >= 1 && newStoneY <= 8) {
                        kingX = nx;
                        kingY = ny;
                        stoneX = newStoneX;
                        stoneY = newStoneY;
                    }
                } else {
                    kingX = nx;
                    kingY = ny;
                }
            }
        }
        // 결과를 문자열로 변환하여 출력
        String kingResult = String.format("%c%d", kingX + 'A' - 1, kingY);
        String stoneResult = String.format("%c%d", stoneX + 'A' - 1, stoneY);
        bw.write(kingResult + "\n");
        bw.write(stoneResult);
        bw.flush();
        bw.close();
        br.close();
    }
}