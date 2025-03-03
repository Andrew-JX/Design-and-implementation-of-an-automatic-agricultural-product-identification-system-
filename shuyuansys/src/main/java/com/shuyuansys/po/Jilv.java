package com.shuyuansys.po;

import java.io.Serializable;

public class Jilv implements Serializable {

      private  Integer  id;
 private  String  title;
 private  String  uptime;
 private  Integer  uid;
 private  String  jie;
 private  String  picurl;

      private String username;


      public  Integer  getId(){
   return   id;
}
 public  void setId( Integer   id){
 this.id=id;
}
 public  String  getTitle(){
   return   title;
}
 public  void setTitle( String   title){
 this.title=title;
}
 public  String  getUptime(){
   return   uptime;
}
 public  void setUptime( String   uptime){
 this.uptime=uptime;
}
 public  Integer  getUid(){
   return   uid;
}
 public  void setUid( Integer   uid){
 this.uid=uid;
}
 public  String  getJie(){
   return   jie;
}
 public  void setJie( String   jie){
 this.jie=jie;
}
 public  String  getPicurl(){
   return   picurl;
}
 public  void setPicurl( String   picurl){
 this.picurl=picurl;
}

    
 public String getUsername(){
   return   username;
}

 public  void setUsername(String  username){
 this.username=username;
}



}