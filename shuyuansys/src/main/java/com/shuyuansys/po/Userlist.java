package com.shuyuansys.po;

import java.io.Serializable;

public class Userlist implements Serializable {

      private  Integer  id;
 private  String  username;
 private  String  password;
 private  String  cname;
 private  String  sex;
 private  String  tel;
 private  String  email;

     

      public  Integer  getId(){
   return   id;
}
 public  void setId( Integer   id){
 this.id=id;
}
 public  String  getUsername(){
   return   username;
}
 public  void setUsername( String   username){
 this.username=username;
}
 public  String  getPassword(){
   return   password;
}
 public  void setPassword( String   password){
 this.password=password;
}
 public  String  getCname(){
   return   cname;
}
 public  void setCname( String   cname){
 this.cname=cname;
}
 public  String  getSex(){
   return   sex;
}
 public  void setSex( String   sex){
 this.sex=sex;
}
 public  String  getTel(){
   return   tel;
}
 public  void setTel( String   tel){
 this.tel=tel;
}
 public  String  getEmail(){
   return   email;
}
 public  void setEmail( String   email){
 this.email=email;
}

    


}