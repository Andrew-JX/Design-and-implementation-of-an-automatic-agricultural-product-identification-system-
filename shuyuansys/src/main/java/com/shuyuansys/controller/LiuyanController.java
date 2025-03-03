
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Liuyan;
import com.shuyuansys.service.LiuyanService;
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
@RequestMapping("/liuyan")
public class LiuyanController {

    @Autowired
    private LiuyanService liuyanService;


    /**
     * 返回Liuyan模型中的列表
     */

    @RequestMapping("/queryLiuyanAll")
    @ResponseBody
    public JsonInfo queryLiuyanAll(
            Liuyan liuyan,
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
        data.put("liuyan", liuyan);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Liuyan> pageInfo = liuyanService.queryLiuyanAll(data);
        return JsonInfo.ok("queryLiuyanAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topLiuyanNumList")
    @ResponseBody
    public JsonInfo topLiuyanNumList(Liuyan liuyan,
                                     @RequestParam(defaultValue = "0") Integer num,
                                     @RequestParam(defaultValue = "") String whstr,
                                     @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("liuyan", liuyan);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Liuyan> list = liuyanService.topLiuyanNumList(data);
        return JsonInfo.ok("topLiuyanNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/queryLiuyanById")
    @ResponseBody
    public JsonInfo queryLiuyanById(Liuyan liuyan, @RequestParam(defaultValue = "0") Integer id) {
        liuyan = liuyanService.queryLiuyanById(id);//根据id查询对象
        return JsonInfo.ok("queryLiuyanById", Constants.OK_MSG, Arrays.asList(liuyan));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteLiuyanByIds")
    @ResponseBody
    public JsonInfo deleteLiuyanByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        liuyanService.deleteLiuyanByIds(list);
        return JsonInfo.ok("deleteLiuyanByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param liuyan
     * @return
     */
    @RequestMapping("/addLiuyanSubmit")
    @ResponseBody
    public JsonInfo addLiuyanSubmit(Liuyan liuyan) {
        String msg = Constants.ERR_MSG;
        try {
            liuyanService.addLiuyanSubmit(liuyan);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addLiuyanSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateLiuyanSubmit")
    @ResponseBody
    public JsonInfo updateLiuyanSubmit(Liuyan liuyan) {
        String msg = Constants.ERR_MSG;
        try {
            liuyanService.updateLiuyanSubmit(liuyan);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateLiuyanSubmit", msg);
    }


}
