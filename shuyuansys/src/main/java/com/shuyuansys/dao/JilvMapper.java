package com.shuyuansys.dao;

import com.shuyuansys.po.Jilv;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;
public interface JilvMapper {
    /**
    删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
   添加全部的
     */
    int insert(Jilv record);

    /**
    添加不为空的
     */
    int insertSelective(Jilv record);

    /**
     查询
     */
    Jilv selectByPrimaryKey(Integer id);

    /**
  修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Jilv record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Jilv record);

    /**
     * 查询
     */
    List<Jilv> queryJilvInfoAll(Map<String,Object> map);

  /*查询列表*/
    List<Jilv> topJilvNumList(Map<String,Object> map);

  List<Jilv> topJilvNumListInTable(Map<String,Object> map);

}