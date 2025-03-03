package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.ArticleMapper;
import com.shuyuansys.po.Article;
import com.shuyuansys.service.ArticleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Map;
import java.util.List;

@Service("articleService")
public class ArticleServiceimpl implements ArticleService {

    @Autowired
    private ArticleMapper articleMapper;

    @Override
    public PageInfo<Article> queryArticleAll(Map<String,Object> map) {

        int page= (int) map.get("page");
        int limit= (int) map.get("limit");
        PageHelper.startPage(page,limit);

        List<Article> articleList = articleMapper.queryArticleInfoAll(map);
        return new PageInfo<>(articleList) ;
    }
  @Override
    public  List<Article> topArticleNumList(Map<String,Object> map)
    {
                 List<Article> toplist=articleMapper.topArticleNumList(map);
                 return  toplist;

     }

  @Override
    public  List<Article> topArticleNumListInTable(Map<String,Object> map)
        {
        List<Article> toplist=articleMapper.topArticleNumList(map);
        return  toplist;

        }

    @Override
    public void addArticleSubmit(Article article) {
        articleMapper.insert(article);
    }

    @Override
    public Article queryArticleById(Integer id) {
        return articleMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateArticleSubmit(Article article) {
        articleMapper.updateByPrimaryKeySelective(article);//修改不为空的字段
    }

    @Override
    public void deleteArticleByIds(List<String> ids) {
        for (String id : ids){
            articleMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


}
