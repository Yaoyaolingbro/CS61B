public class HelloWorld {
    public static int larger(int x,int y) {
        if (x > y) {
            return x;
        } else {
            return y;
        }
    }
    public static void main(String[] atgs) {
        System.out.println(larger(5, 6));
    }
}