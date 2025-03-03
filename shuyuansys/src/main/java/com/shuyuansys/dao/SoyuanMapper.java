package com.shuyuansys.dao;

import com.shuyuansys.po.Soyuan;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;
public interface SoyuanMapper {
    /**
    删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
   添加全部的
     */
    int insert(Soyuan record);

    /**
    添加不为空的
     */
    int insertSelective(Soyuan record);

    /**
     查询
     */
    Soyuan selectByPrimaryKey(Integer id);

    /**
  修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Soyuan record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Soyuan record);

    /**
     * 查询
     */
    List<Soyuan> querySoyuanInfoAll(Map<String,Object> map);

  /*查询列表*/
    List<Soyuan> topSoyuanNumList(Map<String,Object> map);

  List<Soyuan> topSoyuanNumListInTable(Map<String,Object> map);

}