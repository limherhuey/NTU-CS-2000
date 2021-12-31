public class Plane {
    private PlaneSeat[] seat;
    private int numEmptySeat;

    public Plane() {
        seat = new PlaneSeat[12];
        for (int i = 0; i < seat.length; i++) {
            // seatID is set to their position in the array
            seat[i] = new PlaneSeat(i+1);
        }
        numEmptySeat = 12;
    }

    private PlaneSeat[] sortSeats() {
        int i, j, k;

        // make a copy of the array seat
        PlaneSeat[] sorted_seats = new PlaneSeat[seat.length - numEmptySeat];
        for (i = 0, k = 0; i < seat.length; i++) {
            if (seat[i].isOccupied()) {
                sorted_seats[k] = new PlaneSeat(seat[i].getSeatID());
                sorted_seats[k].assign(seat[i].getCustomerID());
                k++;
            }
        }

        // insertion sort
        PlaneSeat s;
        for (i = 1; i < sorted_seats.length; i++) {
            j = i;
            s = sorted_seats[j];
            while (j > 0 && s.getCustomerID() < sorted_seats[j-1].getCustomerID()) {
                sorted_seats[j] = sorted_seats[j-1];
                j--;
            }
            sorted_seats[j] = s;
        }

        return sorted_seats;
    }

    public void showNumEmptySeats() {
        System.out.printf("There are " + numEmptySeat + " empty seats\n");
    }

    public void showEmptySeats() {
        System.out.println("The following seats are empty:");
        for (int i = 0; i < seat.length; i++) {
            if (!seat[i].isOccupied()) {
                System.out.println("SeatID " + seat[i].getSeatID());
            }
        }
    }

    public void showAssignedSeats(boolean bySeatId) {
        System.out.println("The seat assignments are as follows:");
        if (bySeatId) {
            // display sorted by seatID
            for (int i = 0; i < seat.length; i++) {
                if (seat[i].isOccupied()) {
                    System.out.println("SeatID " + seat[i].getSeatID() + " assigned to CustomerID " + seat[i].getCustomerID() + ".");
                }
            }
        } else {
            // display sorted by customerID
            PlaneSeat[] seats_sorted = sortSeats();
            for (int i = 0; i < seats_sorted.length; i++) {
                System.out.println("SeatID " + seats_sorted[i].getSeatID() + " assigned to CustomerID " + seats_sorted[i].getCustomerID() + ".");
            }
        }
    }

    public void assignSeat(int seatId, int cust_id) {
        if (seatId > seat.length || seatId <= 0) {
            System.out.println("Not a valid seat ID!");
            return;
        } else if (seat[seatId-1].isOccupied()) {
            System.out.println("Seat already assigned to a customer.");
            return;
        }

        seat[seatId-1].assign(cust_id);
        numEmptySeat--;
        System.out.println("Seat assigned!");
    }

    public void unAssignSeat(int seatId) {
        if (seatId > seat.length || seatId <= 0) {
            System.out.println("Not a valid seat ID!");
            return;
        } else if (!seat[seatId-1].isOccupied()) {
            System.out.println("Error - Seat wasn't occupied in the first place!");
            return;
        }

        seat[seatId-1].unAssign();
        numEmptySeat++;
        System.out.println("Seat Unassigned!");
    }
}
