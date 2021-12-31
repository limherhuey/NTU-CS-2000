import java.util.Scanner;

public class P3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("starting value: ");
        int start = sc.nextInt();
        System.out.print("ending value: ");
        int end = sc.nextInt();
        System.out.print("increment: ");
        int inc = sc.nextInt();
        sc.close();

        // catch error
        if (start > end) {
            System.out.println("Error input!!");
            return;
        }

        // for loop
        System.out.print("US$\t\tS$\n---------------------\n");
        double usd;
        for (usd = start; usd <= end; usd += inc) {
            System.out.printf("%.0f\t\t%s\n", usd, 1.82 * usd);
        }

        // while loop
        System.out.print("\nUS$\t\tS$\n---------------------\n");
        usd = start;
        while (usd <= end) {
            System.out.printf("%.0f\t\t%s\n", usd, 1.82 * usd);
            usd += inc;
        }

        // do/while loop
        System.out.print("\nUS$\t\tS$\n---------------------\n");
        usd = start;
        do {
            System.out.printf("%.0f\t\t%s\n", usd, 1.82 * usd);
            usd += inc;
        } while (usd <= end);
    }
}
