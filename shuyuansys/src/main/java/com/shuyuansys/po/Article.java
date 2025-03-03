package com.shuyuansys.po;

import java.io.Serializable;

public class Article implements Serializable {

    private Integer id;
    private Integer cid;
    private String title;
    private String picurl;
    private String memo;
    private String uptime;

    private String fenleiname;


    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getCid() {
        return cid;
    }

    public void setCid(Integer cid) {
        this.cid = cid;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getPicurl() {
        return picurl;
    }

    public void setPicurl(String picurl) {
        this.picurl = picurl;
    }

    public String getMemo() {
        return memo;
    }

    public void setMemo(String memo) {
        this.memo = memo;
    }

    public String getUptime() {
        return uptime;
    }

    public void setUptime(String uptime) {
        this.uptime = uptime;
    }


    public String getFenleiname() {
        return fenleiname;
    }

    public void setFenleiname(String fenleiname) {
        this.fenleiname = fenleiname;
    }


}