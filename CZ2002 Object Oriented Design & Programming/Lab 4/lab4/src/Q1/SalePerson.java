package Q1;
public class SalePerson implements Comparable {
    private String firstName;
    private String lastName;
    private int totalSales;

    public SalePerson(String firstName, String lastName, int totalSales) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.totalSales = totalSales;
    }

    public String toString() {
        return lastName + ", " + firstName + " : " + totalSales;
    }

    public boolean equals(Object o) {
        if (this.getClass().equals(o.getClass())) {
            SalePerson sp = (SalePerson) o;
            return firstName == sp.getFirstName() && lastName == sp.getLastName();
        }
        return false;
    }

    public int compareTo(Object o) {
        if (this.getClass().equals(o.getClass())) {
            SalePerson sp = (SalePerson) o;

            // compare total sales
            if (totalSales == sp.getTotalSales()) {
                // same: break tie using last name
                for (int i = 0; i < lastName.length(); i++) {
                    if (lastName.charAt(i) != sp.getLastName().charAt(i)) {
                        return sp.getLastName().charAt(i) - lastName.charAt(i);
                    }
                }
            }
            else {
                return totalSales - sp.getTotalSales();
            }
        }
        return 0;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public int getTotalSales() {
        return totalSales;
    }
}
