public class charSwitch {

    public static void main(String[] args) {
        char myChar = 'Z';
        switch(myChar) {
            case 'A': case 'B': case 'C': case 'D': case 'E':
                System.out.println("Character " + myChar + " was found.");
                break;
            default:
                System.out.println("The character was not found");
                break;
        }
    }
}
