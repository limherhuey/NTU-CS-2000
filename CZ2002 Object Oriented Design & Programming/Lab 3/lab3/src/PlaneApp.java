import java.util.Scanner;

public class PlaneApp {
    public static void main(String[] args) {
        int choice, seatID, custID;
        Scanner sc = new Scanner(System.in);
        Plane p = new Plane();

        System.out.println("1: show the number of empty seats");
        System.out.println("2: show the list of empty seats");
        System.out.println("3: show the list of customers together with their seat numbers in the order of the seat numbers");
        System.out.println("4: show the list of customers together with their seat numbers in the ordre of the customer ID");
        System.out.println("5: assign a customer to a seat");
        System.out.println("6: remove a seat assignment");
        System.out.println("7: quit");

        do {
            System.out.print("\nEnter the number of your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1: p.showNumEmptySeats(); break;
                case 2: p.showEmptySeats(); break;
                case 3: p.showAssignedSeats(true); break;
                case 4: p.showAssignedSeats(false); break;
                case 5:
                    System.out.println("Assigning seat...");
                    System.out.print("Please enter seatID: ");
                    seatID = sc.nextInt();
                    System.out.print("Please enter Customer ID: ");
                    custID = sc.nextInt();
                    p.assignSeat(seatID, custID);
                    break;
                case 6:
                    System.out.print("Enter seatID to unassign customer from: ");
                    seatID = sc.nextInt();
                    p.unAssignSeat(seatID);
                    break;
                case 7:
            }
        } while (choice < 7);
        sc.close();
    }
}
