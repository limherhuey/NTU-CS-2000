import java.util.Scanner;

public class Lab2p1 {
    public static void main(String[] args) {
        int choice, m, n;
        long nlong;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Perform the following methods:");
            System.out.println("1: multiplication test");
            System.out.println("2: quotient using division by substraction");
            System.out.println("3: remainder using division by subtraction");
            System.out.println("4: count the number of digits");
            System.out.println("5: position of a digit");
            System.out.println("6: extract all odd digits");
            System.out.println("7: quit");
            choice = sc.nextInt();

            switch(choice) {
                case 1: mulTest(); break;
                case 2:
                    System.out.print("Divide m by n. Input m and n: ");
                    m = sc.nextInt();
                    n = sc.nextInt();
                    System.out.println(m + "/" + n + " = " + divide(m, n));
                    break;
                case 3:
                    System.out.print("Modulo m by n. Input m and n: ");
                    m = sc.nextInt();
                    n = sc.nextInt();
                    System.out.println(m + " % " + n + " = " + modulus(m, n));
                    break;
                case 4:
                    System.out.print("Count number of digits for a positive integer n. Input n: ");
                    n = sc.nextInt();
                    System.out.print("n: " + n + " - ");
                    if (n <= 0) System.out.println("Error input!!");
                    else System.out.println("count = " + countDigits(n));
                    break;
                case 5:
                    System.out.print("Input positive number n: ");
                    n = sc.nextInt();
                    System.out.print("Input digit to be found: ");
                    m = sc.nextInt();
                    System.out.println("\nposition = " + position(n, m));
                    break;
                case 6:
                    System.out.print("Input positive number n: ");
                    nlong = sc.nextLong();
                    if (nlong <= 0) System.out.println("oddDigits = Error input!!");
                    else System.out.println("oddDigits = " + extractOddDigits(nlong));
                    break;
                case 7: default:
                    System.out.println("Program terminating....");
            }
        } while (choice < 7);
        sc.close();
    }

    public static void mulTest() {
        int Qcount = 5, i;
        int a, b, ans, correct = 0;
        Scanner sc = new Scanner(System.in); // can't close the scanner in methods or it will close System.in input stream in the main method as well

        for (i = 0; i < Qcount; i++) {
            a = 1 + (int) (Math.random() * 9);
            b = 1 + (int) (Math.random() * 9);
            System.out.printf("How much is %d times %d? ", a, b);
            ans = sc.nextInt();
            if (ans == a * b) correct++;
        }

        System.out.printf("%d answers out of %d are correct.\n", correct, Qcount);
    }

    public static int divide(int m, int n) {
        int quotient = 0;
        while (m >= n) {
            m -= n;
            quotient++;
        }
        return quotient;
    }

    public static int modulus(int m, int n) {
        while (m >= n) {
            m -= n;
        }
        return m;
    }

    public static int countDigits(int n) {
        int count = 0;
        while (n > 0) {
            n /= 10;
            count++;
        }
        return count;
    }

    public static int position(int n, int digit) {
        int count = 1;
        while (n > 0) {
            if (digit == n % 10)
                return count;
            n /= 10;
            count ++;
        }
        return -1;
    }

    public static long extractOddDigits(long n) {
        long oddDigits = 0, c = 0;
        int digit;
        while (n > 0) {
            digit = (int) (n % 10);
            if (digit % 2 != 0) {
                oddDigits += digit * (long) Math.pow(10, c);
                c++;
            }
            n /= 10;
        }
        if (oddDigits == 0) return -1;
        return oddDigits;
    }
}
