
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Wenfei;
import com.shuyuansys.service.WenfeiService;
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
@RequestMapping("/wenfei")
public class WenfeiController {

    @Autowired
    private WenfeiService wenfeiService;


    /**
     * 返回Wenfei模型中的列表
     */

    @RequestMapping("/queryWenfeiAll")
    @ResponseBody
    public JsonInfo queryWenfeiAll(
            Wenfei wenfei,
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
        data.put("wenfei", wenfei);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Wenfei> pageInfo = wenfeiService.queryWenfeiAll(data);
        return JsonInfo.ok("queryWenfeiAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topWenfeiNumList")
    @ResponseBody
    public JsonInfo topWenfeiNumList(Wenfei wenfei,
                                     @RequestParam(defaultValue = "0") Integer num,
                                     @RequestParam(defaultValue = "") String whstr,
                                     @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("wenfei", wenfei);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Wenfei> list = wenfeiService.topWenfeiNumList(data);
        return JsonInfo.ok("topWenfeiNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/queryWenfeiById")
    @ResponseBody
    public JsonInfo queryWenfeiById(Wenfei wenfei, @RequestParam(defaultValue = "0") Integer id) {
        wenfei = wenfeiService.queryWenfeiById(id);//根据id查询对象
        return JsonInfo.ok("queryWenfeiById", Constants.OK_MSG, Arrays.asList(wenfei));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteWenfeiByIds")
    @ResponseBody
    public JsonInfo deleteWenfeiByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        wenfeiService.deleteWenfeiByIds(list);
        return JsonInfo.ok("deleteWenfeiByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param wenfei
     * @return
     */
    @RequestMapping("/addWenfeiSubmit")
    @ResponseBody
    public JsonInfo addWenfeiSubmit(Wenfei wenfei) {
        String msg = Constants.ERR_MSG;
        try {
            wenfeiService.addWenfeiSubmit(wenfei);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addWenfeiSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateWenfeiSubmit")
    @ResponseBody
    public JsonInfo updateWenfeiSubmit(Wenfei wenfei) {
        String msg = Constants.ERR_MSG;
        try {
            wenfeiService.updateWenfeiSubmit(wenfei);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateWenfeiSubmit", msg);
    }


}
