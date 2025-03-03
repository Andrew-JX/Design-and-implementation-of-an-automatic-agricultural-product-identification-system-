
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Userlist;
import com.shuyuansys.service.UserlistService;
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
@RequestMapping("/userlist")
public class UserlistController {

    @Autowired
    private UserlistService userlistService;


//----------------------------------------------------------------------------------------

    /**
     * 注册
     *
     * @param userlist
     * @return
     */
    @RequestMapping("/UserlistRegister")
    @ResponseBody
    public JsonInfo UserlistRegister(Userlist userlist, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
//先判断是否有重复的用户
        String whstr = "";
        String username = request.getParameter("username");
        whstr = whstr + " and username='" + username + "'";
        Map<String, Object> data = new HashMap<>();
        data.put("userlist", userlist);
        data.put("limit", "1");
        data.put("orderby", "id");
        data.put("whstr", whstr);
        List<Userlist> list = userlistService.topUserlistNumListInTable(data);
        int u = list.size();
        if (u > 0) {
            msg = Constants.ERR_username_MSG;
        } else {
            //添加
            userlistService.addUserlistSubmit(userlist);
            msg = Constants.OK_MSG;
        }
        return JsonInfo.ok("UserlistRegister", msg);
    }

    /**
     * 登录
     *
     * @param
     * @return
     */
    @RequestMapping("/UserlistLogin")
    @ResponseBody
    public JsonInfo UserlistLogin(Userlist userlist, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        Userlist user = null;
        try {
            String username = request.getParameter("username");
            String password = request.getParameter("password");
            if (username.equals("")) {
                msg = Constants.ERR_MSG;
            } else if (password.equals("")) {
                msg = Constants.ERR_MSG;
            } else {
                userlist.setUsername(username);
                userlist.setPassword(password);
                String whstr = "";
                whstr = whstr + " and username='" + username + "'";
                whstr = whstr + " and password='" + password + "'";
                Map<String, Object> data = new HashMap<String, Object>();
                data.put("userlist", userlist);
                data.put("limit", "0");
                data.put("orderby", "id");
                data.put("whstr", whstr);
                List<Userlist> list = userlistService.topUserlistNumListInTable(data);
                if (list.size() >= 1) {
                    user = (Userlist) list.get(0);
                    //登录成功
                    HttpSession session = request.getSession();
                    session.setAttribute("userlistLogin", user);
                    msg = Constants.OK_MSG;
                }
            }
        } catch (Exception e) {
            //用户名或密码不正确
            msg = Constants.ERR_MSG;
        }
        if (msg.equals(Constants.OK_MSG)) {
            return JsonInfo.ok("UserlistLogin", msg, user);
        } else {
            return JsonInfo.ok("UserlistLogin", msg);
        }
    }

    /**
     * 修改密码
     *
     * @param userlist
     * @return
     */
    @RequestMapping("/UserlistChagePass")
    @ResponseBody
    public JsonInfo UserlistChagePass(Userlist userlist, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        //先判断是否登录
        HttpSession session = request.getSession();
        try {
            if (session.getAttribute("userlistLogin") != null) {
                Userlist user = (Userlist) session.getAttribute("userlistLogin");
                // System.out.println(session.getAttribute("userlistLogin"));
                System.out.println(user.getUsername());
                System.out.println(user.getId());
                //判断旧密码是否正确
                String oldpassword = request.getParameter("oldpassword");
                String password = request.getParameter("password");
                userlist.setPassword(password);
                userlist.setId(user.getId());
                userlist.setUsername(user.getUsername());
                //如果正确就去修改新密码
                try {
                    userlistService.updateUserlistSubmit(userlist);//数据库修改
                    msg = Constants.OK_MSG;
                } catch (Exception e) {
                    msg = Constants.ERR_MSG;
                }
            } else {
                msg = Constants.ERR_adminlogin_MSG;
            }
        } catch (Exception e) {
            msg = Constants.ERR_adminlogin_MSG;
        }
        return JsonInfo.ok("UserlistChagePass", msg);
    }

    /**
     * 判断是否登录
     *
     * @param userlist
     * @return
     */
    @RequestMapping("/UserlistGetLogin")
    @ResponseBody
    public JsonInfo UserlistGetLogin(Userlist userlist, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        HttpSession session = request.getSession();
        try {
            if (session.getAttribute("userlistLogin") != null) {
                msg = Constants.OK_MSG;
            } else {
                msg = Constants.ERR_adminlogin_MSG;
            }
        } catch (Exception e) {
            msg = Constants.ERR_adminlogin_MSG;
        }
        if (msg.equals(Constants.OK_MSG)) {
            Userlist user = (Userlist) session.getAttribute("userlistLogin");
            return JsonInfo.ok("UserlistGetLogin", msg, userlistService.queryUserlistById(user.getId()));
        } else {
            return JsonInfo.ok("UserlistGetLogin", msg);
        }
    }

    /**
     * 退出登录
     *
     * @param userlist
     * @param request
     * @return
     */
    @RequestMapping("/UserlistLogout")
    @ResponseBody
    public JsonInfo UserlistLogout(Userlist userlist, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        try {
            HttpSession session = request.getSession();
            session.invalidate();//注销
            msg = Constants.ERR_adminlogin_MSG;//退出
        } catch (Exception e) {
            msg = Constants.ERR_adminlogin_MSG;
        }
        return JsonInfo.ok("UserlistLogout", msg);
    }
//----------------------------------------------------------------------------------------


    /**
     * 返回Userlist模型中的列表
     */

    @RequestMapping("/queryUserlistAll")
    @ResponseBody
    public JsonInfo queryUserlistAll(
            Userlist userlist,
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
        data.put("userlist", userlist);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Userlist> pageInfo = userlistService.queryUserlistAll(data);
        return JsonInfo.ok("queryUserlistAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topUserlistNumList")
    @ResponseBody
    public JsonInfo topUserlistNumList(Userlist userlist,
                                       @RequestParam(defaultValue = "0") Integer num,
                                       @RequestParam(defaultValue = "") String whstr,
                                       @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("userlist", userlist);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Userlist> list = userlistService.topUserlistNumList(data);
        return JsonInfo.ok("topUserlistNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/queryUserlistById")
    @ResponseBody
    public JsonInfo queryUserlistById(Userlist userlist, @RequestParam(defaultValue = "0") Integer id) {
        userlist = userlistService.queryUserlistById(id);//根据id查询对象
        return JsonInfo.ok("queryUserlistById", Constants.OK_MSG, Arrays.asList(userlist));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteUserlistByIds")
    @ResponseBody
    public JsonInfo deleteUserlistByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        userlistService.deleteUserlistByIds(list);
        return JsonInfo.ok("deleteUserlistByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param userlist
     * @return
     */
    @RequestMapping("/addUserlistSubmit")
    @ResponseBody
    public JsonInfo addUserlistSubmit(Userlist userlist) {
        String msg = Constants.ERR_MSG;
        try {
            userlistService.addUserlistSubmit(userlist);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addUserlistSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateUserlistSubmit")
    @ResponseBody
    public JsonInfo updateUserlistSubmit(Userlist userlist) {
        String msg = Constants.ERR_MSG;
        try {
            userlistService.updateUserlistSubmit(userlist);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateUserlistSubmit", msg);
    }


}
