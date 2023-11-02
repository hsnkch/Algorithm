import java.io.*;
import java.util.*;

public class Main {
    static int time;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        Deque<Integer> trucks = new ArrayDeque<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trucks.offer(Integer.parseInt(st.nextToken()));
        }

        Deque<Integer> bridge = new ArrayDeque<>();
        for (int i = 0; i < w; i++) {
            bridge.offer(0);
        }
        time = 0;

        while (!bridge.isEmpty()) {
            time++;
            bridge.pollFirst();
            if (!trucks.isEmpty()) {
                if (bridge.stream().mapToInt(Integer::intValue).sum() <= l) {
                    bridge.offer(trucks.pollFirst());
                } else {
                    bridge.offer(0);
                }
            }
        }
        bw.write(Integer.toString(time));
        bw.flush();
        bw.close();
        br.close();
    }
}