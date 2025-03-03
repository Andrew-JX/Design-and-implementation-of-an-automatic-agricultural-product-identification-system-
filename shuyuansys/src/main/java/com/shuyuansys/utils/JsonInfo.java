package com.shuyuansys.utils;


import java.io.Serializable;

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
public class JsonInfo implements Serializable {


    private String msg; //返回状态信息
    private Object enlist;//返回记录列表
    private Object entity;//返回页数，条数，页码
    private String act;//返回调用的API接口名称
    private String res; //返回字符串

    public JsonInfo() {


    }

    public JsonInfo(String act, String msg, Integer sumpage, Long count, Integer page, Object enlist) {

        this.entity = new Entity(sumpage, count, page);
        this.msg = msg;
        this.act = act;
        this.enlist = enlist;

    }

    public JsonInfo(String act, String msg, String res) {

        this.msg = msg;
        this.act = act;
        this.res = res;
    }

    public JsonInfo(String act, String msg) {

        this.msg = msg;
        this.act = act;

    }

    //用户于添加保存，修改保存，删除时返回
    public static JsonInfo ok(String act, String msg) {
        return new JsonInfo(act, msg);
    }

    //用户返回字符串
    public static JsonInfo ok(String act, String msg, String res) {
        return new JsonInfo(act, msg, res);
    }

    //返回top条记录
    public static JsonInfo ok(String act, String msg, long count, Object enlist) {
        return new JsonInfo(act, msg, 1, count, 1, enlist);
    }

    //返回id一条记录
    public static JsonInfo ok(String act, String msg, Object enlist) {
        return new JsonInfo(act, msg, 1, (long) 1, 1, enlist);
    }

    //返回分页的记录
    public static JsonInfo ok(String act, String msg, Integer sumpage, Long count, Integer page, Object enlist) {
        return new JsonInfo(act, msg, sumpage, count, page, enlist);
    }

    //
    public static JsonInfo adminnologin() {
        return new JsonInfo("login", "000001");

    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    public Object getEnlist() {
        return enlist;
    }

    public void setEnlist(Object enlist) {
        this.enlist = enlist;
    }

    public Object getEntity() {
        return entity;
    }

    public void setEntity(Object entity) {
        this.entity = entity;
    }


    public String getAct() {
        return act;
    }

    public void setAct(String act) {
        this.act = act;
    }

    public String getRes() {

        return res;
    }

    public void setRes(String res) {
        this.res = res;
    }


}


class Entity implements Serializable {

    private Integer sumpage;//页数
    private Long count;//条数
    private Integer page;//页码

    public Entity() {


    }

    public Entity(Integer sumpage, Long count, Integer page) {

        this.sumpage = sumpage;
        this.count = count;
        this.page = page;

    }


    public Integer getSumpage() {
        return sumpage;
    }

    public void setSumpage(Integer sumpage) {
        this.sumpage = sumpage;
    }

    public Long getCount() {
        return count;
    }

    public void setCount(Long count) {
        this.count = count;
    }

    public Integer getPage() {
        return page;
    }

    public void setPage(Integer page) {
        this.page = page;
    }


}
