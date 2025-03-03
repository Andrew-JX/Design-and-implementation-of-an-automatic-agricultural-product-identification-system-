
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Jilv;
import com.shuyuansys.service.JilvService;
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
@RequestMapping("/jilv")
public class JilvController {

    @Autowired
    private JilvService jilvService;


    /**
     * 返回Jilv模型中的列表
     */

    @RequestMapping("/queryJilvAll")
    @ResponseBody
    public JsonInfo queryJilvAll(
            Jilv jilv,
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
        data.put("jilv", jilv);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Jilv> pageInfo = jilvService.queryJilvAll(data);
        return JsonInfo.ok("queryJilvAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topJilvNumList")
    @ResponseBody
    public JsonInfo topJilvNumList(Jilv jilv,
                                   @RequestParam(defaultValue = "0") Integer num,
                                   @RequestParam(defaultValue = "") String whstr,
                                   @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("jilv", jilv);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Jilv> list = jilvService.topJilvNumList(data);
        return JsonInfo.ok("topJilvNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/queryJilvById")
    @ResponseBody
    public JsonInfo queryJilvById(Jilv jilv, @RequestParam(defaultValue = "0") Integer id) {
        jilv = jilvService.queryJilvById(id);//根据id查询对象
        return JsonInfo.ok("queryJilvById", Constants.OK_MSG, Arrays.asList(jilv));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteJilvByIds")
    @ResponseBody
    public JsonInfo deleteJilvByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        jilvService.deleteJilvByIds(list);
        return JsonInfo.ok("deleteJilvByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param jilv
     * @return
     */
    @RequestMapping("/addJilvSubmit")
    @ResponseBody
    public JsonInfo addJilvSubmit(Jilv jilv) {
        String msg = Constants.ERR_MSG;
        try {
            jilvService.addJilvSubmit(jilv);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addJilvSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateJilvSubmit")
    @ResponseBody
    public JsonInfo updateJilvSubmit(Jilv jilv) {
        String msg = Constants.ERR_MSG;
        try {
            jilvService.updateJilvSubmit(jilv);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateJilvSubmit", msg);
    }


}
