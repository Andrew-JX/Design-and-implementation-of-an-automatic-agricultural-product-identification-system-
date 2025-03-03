
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Article;
import com.shuyuansys.service.ArticleService;
import com.shuyuansys.utils.Constants;
import com.shuyuansys.utils.JsonInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
@RequestMapping("/article")
public class ArticleController {

    @Autowired
    private ArticleService articleService;


    /**
     * 返回Article模型中的列表
     */

    @RequestMapping("/queryArticleAll")
    @ResponseBody
    public JsonInfo queryArticleAll(
            Article article,
            HttpServletRequest request,
            @RequestParam(defaultValue = "1") Integer page,
            @RequestParam(defaultValue = "0") Integer ifso,
            @RequestParam(defaultValue = "20") Integer limit,
            @RequestParam(defaultValue = "id desc") String orderby
    ) {
        /*搜索条件------begin-------*/

        String whstr = "";
        if (ifso.equals(1)) {
            String[] filedarr = request.getParameterValues("filedarr[]");
            String[] hstrarr = request.getParameterValues("hstrarr[]");
            String[] keyarr = request.getParameterValues("keyarr[]");

            for (int i = 0; i < filedarr.length; i++) {
                if (hstrarr[i].equals("like")) {
                    whstr = whstr + " and " + filedarr[i] + "  like '%" + keyarr[i] + "%' ";
                } else if (hstrarr[i].equals("=")) {
                    whstr = whstr + " and " + filedarr[i] + "  = " + keyarr[i] + " ";
                } else {
                    whstr = whstr + " and " + filedarr[i] + hstrarr[i] + "" + keyarr[i] + " ";
                }
            }
            System.out.println("搜索条件=" + whstr);
        }

        /*搜索条件-----End--------*/
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("article", article);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Article> pageInfo = articleService.queryArticleAll(data);
        return JsonInfo.ok("queryArticleAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topArticleNumList")
    @ResponseBody
    public JsonInfo topArticleNumList(Article article,
                                      @RequestParam(defaultValue = "0") Integer num,
                                      @RequestParam(defaultValue = "") String whstr,
                                      @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("article", article);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Article> list = articleService.topArticleNumList(data);
        return JsonInfo.ok("topArticleNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/queryArticleById")
    @ResponseBody
    public JsonInfo queryArticleById(Article article, @RequestParam(defaultValue = "0") Integer id) {
        article = articleService.queryArticleById(id);//根据id查询对象
        return JsonInfo.ok("queryArticleById", Constants.OK_MSG, Arrays.asList(article));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteArticleByIds")
    @ResponseBody
    public JsonInfo deleteArticleByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        articleService.deleteArticleByIds(list);
        return JsonInfo.ok("deleteArticleByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param article
     * @return
     */
    @RequestMapping("/addArticleSubmit")
    @ResponseBody
    public JsonInfo addArticleSubmit(Article article) {
        String msg = Constants.ERR_MSG;
        try {
            articleService.addArticleSubmit(article);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addArticleSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateArticleSubmit")
    @ResponseBody
    public JsonInfo updateArticleSubmit(Article article) {
        String msg = Constants.ERR_MSG;
        try {
            articleService.updateArticleSubmit(article);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateArticleSubmit", msg);
    }


}
