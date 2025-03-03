package com.shuyuansys.po;

import java.io.Serializable;

public class Liuyan implements Serializable {

      private  Integer  id;
 private  Integer  uid;
 private  String  memo;
 private  String  huimemo;
 private  String  uptime;

      private String username;


      public  Integer  getId(){
   return   id;
}
 public  void setId( Integer   id){
 this.id=id;
}
 public  Integer  getUid(){
   return   uid;
}
 public  void setUid( Integer   uid){
 this.uid=uid;
}
 public  String  getMemo(){
   return   memo;
}
 public  void setMemo( String   memo){
 this.memo=memo;
}
 public  String  getHuimemo(){
   return   huimemo;
}
 public  void setHuimemo( String   huimemo){
 this.huimemo=huimemo;
}
 public  String  getUptime(){
   return   uptime;
}
 public  void setUptime( String   uptime){
 this.uptime=uptime;
}

    
 public String getUsername(){
   return   username;
}

 public  void setUsername(String  username){
 this.username=username;
}



}