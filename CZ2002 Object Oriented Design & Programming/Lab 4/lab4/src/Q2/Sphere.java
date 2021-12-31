package Q2;

public class Sphere implements Shape {
    private double radius;

    public Sphere(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double calcArea() {
        return 4 * Math.PI * Math.pow(radius, 2);
    }
}
