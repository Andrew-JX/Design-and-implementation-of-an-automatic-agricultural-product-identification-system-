package com.shuyuansys.dao;

import com.shuyuansys.po.Userlist;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;
public interface UserlistMapper {
    /**
    删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
   添加全部的
     */
    int insert(Userlist record);

    /**
    添加不为空的
     */
    int insertSelective(Userlist record);

    /**
     查询
     */
    Userlist selectByPrimaryKey(Integer id);

    /**
  修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Userlist record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Userlist record);

    /**
     * 查询
     */
    List<Userlist> queryUserlistInfoAll(Map<String,Object> map);

  /*查询列表*/
    List<Userlist> topUserlistNumList(Map<String,Object> map);

  List<Userlist> topUserlistNumListInTable(Map<String,Object> map);

}