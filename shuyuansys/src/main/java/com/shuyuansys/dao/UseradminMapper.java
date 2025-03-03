package com.shuyuansys.dao;

import com.shuyuansys.po.Useradmin;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;
public interface UseradminMapper {
    /**
    删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
   添加全部的
     */
    int insert(Useradmin record);

    /**
    添加不为空的
     */
    int insertSelective(Useradmin record);

    /**
     查询
     */
    Useradmin selectByPrimaryKey(Integer id);

    /**
  修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Useradmin record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Useradmin record);

    /**
     * 查询
     */
    List<Useradmin> queryUseradminInfoAll(Map<String,Object> map);

  /*查询列表*/
    List<Useradmin> topUseradminNumList(Map<String,Object> map);

  List<Useradmin> topUseradminNumListInTable(Map<String,Object> map);

}