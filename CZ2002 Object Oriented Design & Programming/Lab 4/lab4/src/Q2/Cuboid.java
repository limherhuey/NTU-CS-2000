package Q2;

public class Cuboid implements Shape {
    private double length;
    private double breadth;
    private double height;

    public Cuboid(double length, double breadth, double height) {
        this.length = length;
        this.breadth = breadth;
        this.height = height;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getBreadth() {
        return breadth;
    }

    public void setBreadth(double breadth) {
        this.breadth = breadth;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double calcArea() {
        Rectangle r1 = new Rectangle(length, breadth);
        Rectangle r2 = new Rectangle(length, height);
        Rectangle r3 = new Rectangle(height, breadth);
        return 2 * r1.calcArea() + 2*  r2.calcArea() + 2 * r3.calcArea();
    }
}
