package Q2;

public class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double calcPerimeter() {
        return 2 * Math.PI * radius;
    }

    public double calcArea() {
        return Math.PI * Math.pow(radius, 2);
    }
}
