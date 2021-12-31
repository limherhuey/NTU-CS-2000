package Q2;

public class Pyramid implements Shape {
    private double baseLength;
    private double baseWidth;
    private double height;
    
    public Pyramid(double height, double baseLength, double baseWidth) {
        this.baseLength = baseLength;
        this.baseWidth = baseWidth;
        this.height = height;
    }

    public double getbaseLength() {
        return baseLength;
    }

    public void setbaseLength(double baseLength) {
        this.baseLength = baseLength;
    }

    public double getbaseWidth() {
        return baseWidth;
    }

    public void setbaseWidth(double baseWdith) {
        this.baseWidth = baseWdith;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double calcArea() {
        double h1 = Math.sqrt(Math.pow(baseWidth/2.0, 2) + Math.pow(height, 2));
        double h2 = Math.sqrt(Math.pow(baseLength/2.0, 2) + Math.pow(height, 2));
        Triangle t1 = new Triangle(baseLength, h1);
        Triangle t2 = new Triangle(baseWidth, h2);
        Rectangle r = new Rectangle(baseLength, baseWidth);
        return 2 * t1.calcArea() + 2 * t2.calcArea() + r.calcArea();
    }
}
