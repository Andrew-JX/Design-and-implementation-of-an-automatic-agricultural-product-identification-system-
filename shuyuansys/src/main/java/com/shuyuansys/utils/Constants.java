package com.shuyuansys.utils;
 

public class Constants {
/*

JSON数据说明
Enlist 为返回的列表
Entity 返回执行后的一些数据
Msg 返回状态代码
000000  失败
000001   管理员没有登录
000005   账号已成在
000003  旧密码输入错误
666666  为执行成功！
100000 返回列表失败
100001 添加失败
100002 修改失败
100003 删除失败
100008	不能为空
Act 当前执行的APi接口

 */
    public final static String OK_MSG = "666666";    //666666表示Ok
    public final static String ERR_MSG = "000000";    //000000表示失败
    public final static String ERR_adminlogin_MSG = "000001";    //管理员没有登录
    public final static String ERR_username_MSG ="000005";// 账号已成在

}
