package Q2;

import java.util.Scanner;

public class Shape2DApp {
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
            System.out.print("\nChoices of shapes:\n1) Square\n2) Rectangle\n3) Circle\n4) Triangle\n");
            System.out.print("Enter the shape of your choice: ");
            do {
                choiceShape = sc.nextInt();
            } while (choiceShape < 1 && choiceShape > 4);

            switch(choiceShape) {
                case 1:
                    System.out.print("Enter the length of sides of the square: ");
                    do {
                        l = sc.nextDouble();
                    } while (l <= 0);
                    Square sq = new Square(l);
                    totalArea += sq.calcArea();
                    break;
                case 2:
                    System.out.print("Enter the length and breadth of the rectangle: ");
                    do {
                        l = sc.nextDouble();
                        b = sc.nextDouble();
                    } while (l <= 0 && b <= 0);
                    Rectangle rt = new Rectangle(l, b);
                    totalArea += rt.calcArea();
                    break;
                case 3:
                    System.out.print("Enter the radius of the circle: ");
                    do {
                        r = sc.nextDouble();
                    } while (r <= 0);
                    Circle cc = new Circle(r);
                    totalArea += cc.calcArea();
                    break;
                case 4:
                    System.out.print("Enter the height and base of the triangle: ");
                    do {
                        h = sc.nextDouble();
                        b = sc.nextDouble();
                    } while (h <= 0 && b <= 0);
                    Triangle tr = new Triangle(h, b);
                    totalArea += tr.calcArea();
                    break;
            }
        }

        System.out.println("The total area of all 2D shapes is " + Math.round(totalArea * 100.0) / 100.0 + " unit^2.");
        sc.close();
    }
}
