import java.io.*;

import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans = 0;

        for (int i = n; i <= 1000001; i++) {
            if (i == 1) {
                continue;
            }
            if (palindrome(i)){
                if (find(i)) {
                    ans = i;
                    break;
                }
            }
        }

        if (ans == 0) {
            ans = 1003001;
        }
        System.out.println(ans);
    }

    public static boolean find(int n) {
        for (int i = 2; i < sqrt(n)+1; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean palindrome(int n) {
        String N = String.valueOf(n);
        StringBuilder sb = new StringBuilder(N);
        String reverse = sb.reverse().toString();
        return N.equals(reverse);
    }


}