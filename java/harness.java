public class ReverseString {

public static String reverse ( String s ) {
    int length = s.length(), last = length - 1;
    char[] chars = s.toCharArray();
    for ( int i = 0; i < length/2; i++ ) {
	char c = chars[i];
	chars[i] = chars[last - i];
	chars[last - i] = c;
    }
    return new String(chars);
}

public static void main ( String[] args ) {
    //for ( int i = 0; i < 10; i++ ) {
    //	System.out.print ( fib(i) + ", " );
    //}
    //System.out.println ( fib(10) );
    System.out.println( reverse( "hello" ) );
}

}