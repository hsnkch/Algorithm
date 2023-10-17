import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] note1 = new int[N];
            for (int j = 0; j < N; j++) {
                note1[j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(note1);
            int M = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] note2 = new int[M];
            for (int k = 0; k < M; k++) {
                note2[k] = Integer.parseInt(st.nextToken());
            }
            for (int num:note2) {
                System.out.println(binarySearch(num,note1));
            }
        }
    }

    public static int binarySearch(int num, int[] note){
        int start = 0;
        int end = note.length - 1;
        while (start <= end){
            int mid = (start + end) / 2;
            if(note[mid] > num){
                end = mid - 1;
            } else if (note[mid] < num) {
                start = mid + 1;
            } else {
                return 1;
            }
        }
        return 0;
    }
}
