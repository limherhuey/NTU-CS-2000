import java.util.Scanner;

public class P2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("salary: ");
        float salary = sc.nextFloat();
        System.out.print("merit: ");
        float merit = sc.nextFloat();
        sc.close();

        if (salary >= 500 && salary <= 599 || salary >= 600 && salary <= 649 && merit < 10) {
            System.out.println("Grade C");
        }
        else if (salary >= 600 && salary <= 649 || salary >= 600 && salary <= 699 || salary >= 700 && salary <= 799 && merit < 20) {
            System.out.println("Grade B");
        }
        else if (salary >= 700 && salary <= 899) {
            System.out.println("Grade A");
        }
    }
}
