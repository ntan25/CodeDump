package com.company;

public class Main {

    public static void main(String[] args) {
        String name = "Joe";

        int score = 800;
        int output2 = calculateHighScorePosition(1298);
        String output = displayHighScorePosition(name, output2);
        System.out.println(output);

//        calculateHighScorePosition();
    }
    public static String displayHighScorePosition(String name, int position) {
        System.out.println(name + " managed to get to position " + position + " on the high score table");
        return "";
    }

    public static int calculateHighScorePosition(int score) {
        if (score >= 1000) {
            return 1;
        } else if (score >= 500) {
            return 2;
        } else if (score >= 100) {
            return 3;
        } else {
            return 4;
        }

    }
}
