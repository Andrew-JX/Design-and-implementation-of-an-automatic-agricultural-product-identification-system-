package com.shuyuansys.dao;

import com.shuyuansys.po.Liuyan;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;
public interface LiuyanMapper {
    /**
    删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
   添加全部的
     */
    int insert(Liuyan record);

    /**
    添加不为空的
     */
    int insertSelective(Liuyan record);

    /**
     查询
     */
    Liuyan selectByPrimaryKey(Integer id);

    /**
  修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Liuyan record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Liuyan record);

    /**
     * 查询
     */
    List<Liuyan> queryLiuyanInfoAll(Map<String,Object> map);

  /*查询列表*/
    List<Liuyan> topLiuyanNumList(Map<String,Object> map);

  List<Liuyan> topLiuyanNumListInTable(Map<String,Object> map);

}