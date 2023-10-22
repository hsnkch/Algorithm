import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long[] cards = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(cards);

        while (m > 0) {
            long tmp = cards[0] + cards[1];
            cards[0] = tmp;
            cards[1] = tmp;
            Arrays.sort(cards);
            m--;
        }
        long sum = 0;
        for (long card : cards) {
            sum += card;
        }

        System.out.println(sum);

    }
}
