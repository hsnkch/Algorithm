import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] house = new int[n];
        for (int i = 0; i < n; i++) {
            house[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(house);
        System.out.println(house[(n-1)/2]);
    }
}