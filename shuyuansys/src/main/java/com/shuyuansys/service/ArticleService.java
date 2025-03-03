package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Article;

import java.util.List;
import java.util.Map;

public interface ArticleService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Article> queryArticleAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Article> topArticleNumList(Map<String,Object> map);

   List<Article> topArticleNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addArticleSubmit(Article article);

    /**
     * 根据id查询（修改）
     */
    Article queryArticleById(Integer id);

    /**
     * 修改提交
     */
    void updateArticleSubmit(Article article);

    /**
     * 删除
     */
    void deleteArticleByIds(List<String> ids);


}
