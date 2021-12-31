import java.util.Scanner;

public class P4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Height: ");
        int height = sc.nextInt();
        sc.close();

        if (height <= 0) {
            System.out.println("Error input!!");
        }

        for (int i = 0; i < height; i++) {
            for (int j = i; j >= 0; j--) {
                if (j % 2 == 0) {
                    System.out.print("AA");
                } else {
                    System.out.print("BB");
                }
            }
            System.out.print("\n");
        }
    }
}
