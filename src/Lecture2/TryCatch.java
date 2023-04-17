package Lecture2;

import java.io.FileReader;
import java.io.IOException;

public class TryCatch {
//    public static void main(String[] args) {
//        int number = 1;
//        try {
//            number = 10 / 0;
//        } catch (ArithmeticException e) {
//            System.out.println("На ноль делить нельзя!");
//        }
//        System.out.println(number);
//    }

    public static void main(String[] args) {
        FileReader test = null;
        try {
            test = new FileReader("test");
            test.read();
        } catch (RuntimeException | IOException e) {
            System.out.println("catch Exception" + e.getClass().getSimpleName());
        } finally {
            System.out.println("Finally start");
            if (test != null) {
                try {
                    test.close();
                } catch (IOException e) {
                    System.out.println("Exception while close");
                }
            }
            System.out.println("Finally finished");
        }
    }
}
