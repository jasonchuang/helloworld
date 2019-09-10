package com.jasonsoft;

import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {


    private static HashMap<Character, Character> map = new HashMap<>();
    static {
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
    }

   /* private static HashMap<Character, Character> map2 = new HashMap<>();
    static {
        map2.put(')', ')');
        map2.put(']', ']');
        map2.put('}', '}');
    }
*/
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (map.containsKey(ch)) {
                stack.push(ch);
            } else if (stack.empty() || map.get(stack.pop()) != ch) {
                return false;
            }
        }

        return stack.isEmpty();
    }


}
