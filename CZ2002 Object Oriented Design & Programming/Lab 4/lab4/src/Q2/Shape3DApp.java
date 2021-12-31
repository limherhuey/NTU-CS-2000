package Q2;

import java.util.Scanner;

public class Shape3DApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numShapes, choiceShape;
        double totalArea = 0;
        double l, b, h, r;

        System.out.print("Enter the total number of shapes: ");
        do {
            numShapes = sc.nextInt();
        } while (numShapes <= 0);

        for (int i = 0; i < numShapes; i++) {
            System.out.print("\nChoices of shapes:\n1) Cuboid\n2) Sphere\n3) Pyramid\n4) Cone\n5) Cylinder\n");
            System.out.print("Enter the shape of your choice: ");
            do {
                choiceShape = sc.nextInt();
            } while (choiceShape < 1 && choiceShape > 3);

            switch(choiceShape) {
                case 1:
                    System.out.print("Enter the length, breadth, and height of the cuboid: ");
                    do {
                        l = sc.nextDouble();
                        b = sc.nextDouble();
                        h = sc.nextDouble();
                    } while (l <= 0 && b <= 0 && h <= 0);
                    Cuboid cb = new Cuboid(l, b, h);
                    totalArea += cb.calcArea();
                    break;
                case 2:
                    System.out.print("Enter the radius of the sphere: ");
                    do {
                        r = sc.nextDouble();
                    } while (r <= 0);
                    Sphere sph = new Sphere(r);
                    totalArea += sph.calcArea();
                    break;
                case 3:
                    System.out.print("Enter the height, base length, and base width of the pyramid: ");
                    do {
                        h = sc.nextDouble();
                        l = sc.nextDouble();
                        b = sc.nextDouble();
                    } while (h <= 0 && l <= 0 && b <= 0);
                    Pyramid py = new Pyramid(h, l, b);
                    totalArea += py.calcArea();
                    break;
                case 4:
                    System.out.print("Enter the radius and height of the cone: ");
                    do {
                        r = sc.nextDouble();
                        h = sc.nextDouble();
                    } while (r <= 0 && h <= 0);
                    Cone c = new Cone(r, h);
                    totalArea += c.calcArea();
                    break;
                case 5:
                    System.out.print("Enter the radius and height of the cylinder: ");
                    do {
                        r = sc.nextDouble();
                        h = sc.nextDouble();
                    } while (r <= 0 && h <= 0);
                    Cylinder cy = new Cylinder(r, h);
                    totalArea += cy.calcArea();
                    break;
            }
        }

        System.out.println("The total surface area of all 3D shapes is " + Math.round(totalArea * 100.0) / 100.0 + " unit^2.");
        sc.close();
    }
}
