package com.shuyuansys.dao;

import com.shuyuansys.po.Article;
import org.apache.ibatis.annotations.Param;

import java.util.List;
import java.util.Map;

public interface ArticleMapper {
    /**
     * 删除
     */
    int deleteByPrimaryKey(Integer id);

    /**
     * 添加全部的
     */
    int insert(Article record);

    /**
     * 添加不为空的
     */
    int insertSelective(Article record);

    /**
     * 查询
     */
    Article selectByPrimaryKey(Integer id);

    /**
     * 修改//修改不为空的字段
     */
    int updateByPrimaryKeySelective(Article record);

    /*
    修改全部字段
     */
    int updateByPrimaryKey(Article record);

    /**
     * 查询
     */
    List<Article> queryArticleInfoAll(Map<String, Object> map);

    /*查询列表*/
    List<Article> topArticleNumList(Map<String, Object> map);

    List<Article> topArticleNumListInTable(Map<String, Object> map);

}