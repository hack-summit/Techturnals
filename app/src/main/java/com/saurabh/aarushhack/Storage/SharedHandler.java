package com.saurabh.aarushhack.Storage;

import android.content.Context;
import android.content.SharedPreferences;

public class SharedHandler {

    public static String DatabaseName = "DATABASE";

    public static void saveValue(Context context, String key, String value) {
        SharedPreferences sharedPreferences = context.getSharedPreferences(DatabaseName, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putString(key, value);
        editor.commit();
    }

    public static String getValue(Context context, String key) {
        SharedPreferences sharedPreferences = context.getSharedPreferences(DatabaseName, Context.MODE_PRIVATE);
        return sharedPreferences.getString(key, "");
    }
}
