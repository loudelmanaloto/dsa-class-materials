import java.util.ArrayList;
import java.util.HashMap;

/**
 * GAME DEV PRACTICE SET - fill in each method below.
 *
 * How to check your work (in the terminal, inside this folder):
 *     javac Practice.java Checker.java SortedScores.java
 *     java Checker
 *
 * Rules:
 *   - Edit ONLY this file (Practice.java).
 *   - Methods must RETURN their answer, not print it.
 *   - Some problems ban certain shortcuts. The checker will tell you.
 *   - Replace the line  throw new UnsupportedOperationException("TODO");
 *     with your own code. Problems you haven't started show as "not started".
 *   - If the checker seems stuck, you probably have an infinite loop.
 *     Press Ctrl + C to stop it.
 */
public class Practice {

    // 1. Playtime clock
    // Games show playtime as "HH:MM:SS". Given a number of seconds, return
    // it as a String. Each part has exactly 2 digits (pad with a zero).
    // Hint: / and % split seconds into hours, minutes, seconds.
    //       String.format("%02d", 5) gives "05".
    // Example: formatPlaytime(3725) -> "01:02:05"
    public static String formatPlaytime(int totalSeconds) {
        throw new UnsupportedOperationException("TODO");
    }

    // 2. Take damage
    // An attack hits for `damage`, but armor soaks up some of it:
    //     actual damage = damage - armor
    // Armor can never HEAL you (actual damage is never below 0), and health
    // can never go below 0. Return the player's new health.
    // Example: applyDamage(100, 30, 10) -> 80
    //          applyDamage(100, 5, 10)  -> 100
    //          applyDamage(20, 50, 0)   -> 0
    public static int applyDamage(int health, int damage, int armor) {
        throw new UnsupportedOperationException("TODO");
    }

    // 3. Rewind
    // Return a NEW array with the items in reverse order (a replay played
    // backwards). Do not change the original array.
    // Not allowed: Collections, or any method named reverse
    // Example: reverseArray({1, 2, 3}) -> {3, 2, 1}
    public static int[] reverseArray(int[] arr) {
        throw new UnsupportedOperationException("TODO");
    }

    // 4. Strongest enemy
    // power[i] is how strong enemy i is. Return the INDEX of the strongest
    // enemy. If there is a tie, return the first one. If the array is
    // empty, return -1.
    // Not allowed: sorting (anything with "sort"), or streams
    // Example: strongestEnemyIndex({40, 90, 55, 90}) -> 1
    public static int strongestEnemyIndex(int[] power) {
        throw new UnsupportedOperationException("TODO");
    }

    // 5. Tidy the loot
    // Return a new list with duplicate items removed, keeping the original
    // order (the first time each item appears). Names are case-sensitive.
    // Do not change the list that was passed in.
    // Example: uniqueItems(["sword", "potion", "sword", "key", "potion"])
    //          -> ["sword", "potion", "key"]
    public static ArrayList<String> uniqueItems(ArrayList<String> items) {
        throw new UnsupportedOperationException("TODO");
    }

    // 6. Same inventory?
    // Two players list what they carry. Return true if they carry exactly
    // the same items, in any order, ignoring upper/lower case. An item that
    // appears twice must appear twice in both. Otherwise return false.
    // Example: sameInventory({"Sword", "Potion"}, {"potion", "SWORD"})
    //          -> true
    public static boolean sameInventory(String[] a, String[] b) {
        throw new UnsupportedOperationException("TODO");
    }

    // 7. Find a score (binary search)
    // `scores` holds high scores ALREADY SORTED from smallest to largest.
    // You can only use:   scores.size()   and   scores.get(i)
    // Return the index where target is found, or -1 if it isn't there.
    // Use BINARY SEARCH: look at the middle, then throw away half each time.
    // (The checker counts how many items you look at. Looping through
    // everything will fail the big test.)
    // Example: scores {0, 12, 24, 48, 96}:  findScore(scores, 48) -> 3
    //                                       findScore(scores, 50) -> -1
    public static int findScore(SortedScores scores, int target) {
        throw new UnsupportedOperationException("TODO");
    }

    // 8. Count the drops
    // Monsters drop loot: {"gold", "gem", "gold", "potion", "gold"}.
    // Return a HashMap of how many times each item dropped.
    // Example: countDrops({"gold", "gem", "gold"}) -> {gold=2, gem=1}
    public static HashMap<String, Integer> countDrops(String[] drops) {
        throw new UnsupportedOperationException("TODO");
    }

    // 9. Poison (recursion)
    // Poison hurts for `damage` this turn, then 1 less each turn after that,
    // until it fades out. Return the TOTAL damage.
    // You MUST solve it recursively (the method calls itself, no loops).
    // Example: totalPoisonDamage(3) -> 6   (3 + 2 + 1)
    //          totalPoisonDamage(5) -> 15  (5 + 4 + 3 + 2 + 1)
    //          totalPoisonDamage(0) -> 0
    public static int totalPoisonDamage(int damage) {
        throw new UnsupportedOperationException("TODO");
    }

    // 10. CHALLENGE: Chests inside chests (recursion)
    // A chest holds items (Strings) and other chests (Object[] arrays),
    // and those can hold more chests. Return the total number of items
    // (Strings) anywhere inside. You MUST solve it recursively.
    // Example: countItems(new Object[]{"sword", new Object[]{"gem", "key"}})
    //          -> 3
    // Hint: for each thing in the chest, is it a String or an Object[]?
    //       thing instanceof Object[] tells you.
    //       To use it as an array: (Object[]) thing
    public static int countItems(Object[] chest) {
        throw new UnsupportedOperationException("TODO");
    }
}
