package Q2;

public class Cone implements Shape {
    private double radius;
    private double height;

    public Cone(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double calcArea() {
        Circle c = new Circle(radius);
        return c.calcArea() + Math.PI * radius * Math.sqrt(Math.pow(height, 2) + Math.pow(radius, 2));
    }
}
