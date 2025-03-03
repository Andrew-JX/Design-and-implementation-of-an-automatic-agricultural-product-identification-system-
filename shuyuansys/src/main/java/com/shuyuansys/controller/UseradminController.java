
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Useradmin;
import com.shuyuansys.service.UseradminService;
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
@RequestMapping("/useradmin")
public class UseradminController {

    @Autowired
    private UseradminService useradminService;


//----------------------------------------------------------------------------------------

    /**
     * 注册
     *
     * @param useradmin
     * @return
     */
    @RequestMapping("/UseradminRegister")
    @ResponseBody
    public JsonInfo UseradminRegister(Useradmin useradmin, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
//先判断是否有重复的用户
        String whstr = "";
        String username = request.getParameter("username");
        whstr = whstr + " and username='" + username + "'";
        Map<String, Object> data = new HashMap<>();
        data.put("useradmin", useradmin);
        data.put("limit", "1");
        data.put("orderby", "id");
        data.put("whstr", whstr);
        List<Useradmin> list = useradminService.topUseradminNumListInTable(data);
        int u = list.size();
        if (u > 0) {
            msg = Constants.ERR_username_MSG;
        } else {
            //添加
            useradminService.addUseradminSubmit(useradmin);
            msg = Constants.OK_MSG;
        }
        return JsonInfo.ok("UseradminRegister", msg);
    }

    /**
     * 登录
     *
     * @param
     * @return
     */
    @RequestMapping("/UseradminLogin")
    @ResponseBody
    public JsonInfo UseradminLogin(Useradmin useradmin, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        Useradmin user = null;
        try {
            String username = request.getParameter("username");
            String password = request.getParameter("password");
            if (username.equals("")) {
                msg = Constants.ERR_MSG;
            } else if (password.equals("")) {
                msg = Constants.ERR_MSG;
            } else {
                useradmin.setUsername(username);
                useradmin.setPassword(password);
                String whstr = "";
                whstr = whstr + " and username='" + username + "'";
                whstr = whstr + " and password='" + password + "'";
                Map<String, Object> data = new HashMap<String, Object>();
                data.put("useradmin", useradmin);
                data.put("limit", "0");
                data.put("orderby", "id");
                data.put("whstr", whstr);
                List<Useradmin> list = useradminService.topUseradminNumListInTable(data);
                if (list.size() >= 1) {
                    user = (Useradmin) list.get(0);
                    //登录成功
                    HttpSession session = request.getSession();
                    session.setAttribute("useradminLogin", user);
                    msg = Constants.OK_MSG;
                }
            }
        } catch (Exception e) {
            //用户名或密码不正确
            msg = Constants.ERR_MSG;
        }
        if (msg.equals(Constants.OK_MSG)) {
            return JsonInfo.ok("UseradminLogin", msg, user);
        } else {
            return JsonInfo.ok("UseradminLogin", msg);
        }
    }

    /**
     * 修改密码
     *
     * @param useradmin
     * @return
     */
    @RequestMapping("/UseradminChagePass")
    @ResponseBody
    public JsonInfo UseradminChagePass(Useradmin useradmin, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        //先判断是否登录
        HttpSession session = request.getSession();
        try {
            if (session.getAttribute("useradminLogin") != null) {
                Useradmin user = (Useradmin) session.getAttribute("useradminLogin");
                // System.out.println(session.getAttribute("useradminLogin"));
                System.out.println(user.getUsername());
                System.out.println(user.getId());
                //判断旧密码是否正确
                String oldpassword = request.getParameter("oldpassword");
                String password = request.getParameter("password");
                useradmin.setPassword(password);
                useradmin.setId(user.getId());
                useradmin.setUsername(user.getUsername());
                //如果正确就去修改新密码
                try {
                    useradminService.updateUseradminSubmit(useradmin);//数据库修改
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
        return JsonInfo.ok("UseradminChagePass", msg);
    }

    /**
     * 判断是否登录
     *
     * @param useradmin
     * @return
     */
    @RequestMapping("/UseradminGetLogin")
    @ResponseBody
    public JsonInfo UseradminGetLogin(Useradmin useradmin, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        HttpSession session = request.getSession();
        try {
            if (session.getAttribute("useradminLogin") != null) {
                msg = Constants.OK_MSG;
            } else {
                msg = Constants.ERR_adminlogin_MSG;
            }
        } catch (Exception e) {
            msg = Constants.ERR_adminlogin_MSG;
        }
        if (msg.equals(Constants.OK_MSG)) {
            Useradmin user = (Useradmin) session.getAttribute("useradminLogin");
            return JsonInfo.ok("UseradminGetLogin", msg, useradminService.queryUseradminById(user.getId()));
        } else {
            return JsonInfo.ok("UseradminGetLogin", msg);
        }
    }

    /**
     * 退出登录
     *
     * @param useradmin
     * @param request
     * @return
     */
    @RequestMapping("/UseradminLogout")
    @ResponseBody
    public JsonInfo UseradminLogout(Useradmin useradmin, HttpServletRequest request) {
        String msg = Constants.ERR_MSG;
        try {
            HttpSession session = request.getSession();
            session.invalidate();//注销
            msg = Constants.ERR_adminlogin_MSG;//退出
        } catch (Exception e) {
            msg = Constants.ERR_adminlogin_MSG;
        }
        return JsonInfo.ok("UseradminLogout", msg);
    }
//----------------------------------------------------------------------------------------


    /**
     * 返回Useradmin模型中的列表
     */

    @RequestMapping("/queryUseradminAll")
    @ResponseBody
    public JsonInfo queryUseradminAll(
            Useradmin useradmin,
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
        data.put("useradmin", useradmin);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Useradmin> pageInfo = useradminService.queryUseradminAll(data);
        return JsonInfo.ok("queryUseradminAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topUseradminNumList")
    @ResponseBody
    public JsonInfo topUseradminNumList(Useradmin useradmin,
                                        @RequestParam(defaultValue = "0") Integer num,
                                        @RequestParam(defaultValue = "") String whstr,
                                        @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("useradmin", useradmin);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Useradmin> list = useradminService.topUseradminNumList(data);
        return JsonInfo.ok("topUseradminNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/queryUseradminById")
    @ResponseBody
    public JsonInfo queryUseradminById(Useradmin useradmin, @RequestParam(defaultValue = "0") Integer id) {
        useradmin = useradminService.queryUseradminById(id);//根据id查询对象
        return JsonInfo.ok("queryUseradminById", Constants.OK_MSG, Arrays.asList(useradmin));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteUseradminByIds")
    @ResponseBody
    public JsonInfo deleteUseradminByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        useradminService.deleteUseradminByIds(list);
        return JsonInfo.ok("deleteUseradminByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param useradmin
     * @return
     */
    @RequestMapping("/addUseradminSubmit")
    @ResponseBody
    public JsonInfo addUseradminSubmit(Useradmin useradmin) {
        String msg = Constants.ERR_MSG;
        try {
            useradminService.addUseradminSubmit(useradmin);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addUseradminSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateUseradminSubmit")
    @ResponseBody
    public JsonInfo updateUseradminSubmit(Useradmin useradmin) {
        String msg = Constants.ERR_MSG;
        try {
            useradminService.updateUseradminSubmit(useradmin);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateUseradminSubmit", msg);
    }


}
