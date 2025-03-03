package com.shuyuansys.dao;

import com.shuyuansys.po.Wenfei;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;
public interface WenfeiMapper {
    /**
    删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
   添加全部的
     */
    int insert(Wenfei record);

    /**
    添加不为空的
     */
    int insertSelective(Wenfei record);

    /**
     查询
     */
    Wenfei selectByPrimaryKey(Integer id);

    /**
  修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Wenfei record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Wenfei record);

    /**
     * 查询
     */
    List<Wenfei> queryWenfeiInfoAll(Map<String,Object> map);

  /*查询列表*/
    List<Wenfei> topWenfeiNumList(Map<String,Object> map);

  List<Wenfei> topWenfeiNumListInTable(Map<String,Object> map);

}