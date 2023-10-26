import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    static int n, d, k, c;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String[] dna = new String[n];
        for (int i = 0; i < n; i++) {
            dna[i] = br.readLine();
        }

        int cnt = 0;

        for (int i = 0; i < m; i++) {
            int[] count = {0, 0, 0, 0};
            for (int j = 0; j < n; j++) {
                switch (dna[j].charAt(i)) {
                    case 'A':
                        count[0]++;
                        break;
                    case 'C':
                        count[1]++;
                        break;
                    case 'G':
                        count[2]++;
                        break;
                    case 'T':
                        count[3]++;
                        break;
                }
            }
            int idx = IntStream.range(0, count.length).reduce((a,b) -> count[a] > count[b]? a : b).getAsInt();
            switch (idx) {
                case 0:
                    bw.append('A');
                    break;
                case 1:
                    bw.append('C');
                    break;
                case 2:
                    bw.append('G');
                    break;
                case 3:
                    bw.append('T');
                    break;
            }
            cnt += n - Arrays.stream(count).max().getAsInt();
        }
        bw.append("\n");
        bw.append(Integer.toString(cnt));
        bw.flush();
        bw.close();
        br.close();
    }
}
