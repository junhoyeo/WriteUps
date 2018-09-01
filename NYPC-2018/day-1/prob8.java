import java.util.Scanner;

public class test8 {
    
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int x = scn.nextInt();
        int y = scn.nextInt();
        rec(x, y, 1, 1);
        if (x == 1 && y == 0){
            System.out.println("POSSIBLE");
            System.exit(0);
        }
        System.out.println("IMPOSSIBLE");
    }

    public static void rec (int x, int y, int a, int b) {
        if (a > x || b > y)
            return;
        if (a == x && b == y){
            System.out.println("POSSIBLE");
            System.exit(0);
        }
        rec(x, y, btn(a, b), b);
        rec(x, y, a, btn(a, b));
    }
    
    public static int btn (int a, int b) {
        return a + b;
    }

}
 