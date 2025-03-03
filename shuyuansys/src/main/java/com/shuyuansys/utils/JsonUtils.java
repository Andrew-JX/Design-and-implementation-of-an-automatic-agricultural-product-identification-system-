package com.shuyuansys.utils;
 
import java.io.IOException;

import javax.servlet.http.HttpServletResponse;

public class JsonUtils {
    public static void ajaxJson(String jsonString,HttpServletResponse response) {
        ajax(jsonString, "application/json",response);
    }
    public static void ajax(String content, String type,HttpServletResponse response) {
        try {
            response.setContentType(type + ";charset=UTF-8");
            response.setHeader("Pragma", "No-cache");
            response.setHeader("Cache-Control", "no-cache");
            response.setDateHeader("Expires", 0);
            response.getWriter().write(content);
            response.getWriter().flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}