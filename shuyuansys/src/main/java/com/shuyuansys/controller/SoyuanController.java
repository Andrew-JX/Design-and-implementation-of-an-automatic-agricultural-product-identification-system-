
package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Soyuan;
import com.shuyuansys.service.SoyuanService;
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

//二维码-------------------

import com.google.zxing.WriterException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;


@Controller
@RequestMapping("/soyuan")
public class SoyuanController {

    @Autowired
    private SoyuanService soyuanService;


    /**
     * 返回Soyuan模型中的列表
     */

    @RequestMapping("/querySoyuanAll")
    @ResponseBody
    public JsonInfo querySoyuanAll(
            Soyuan soyuan,
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
        data.put("soyuan", soyuan);
        data.put("whstr", whstr);
        data.put("page", page);
        data.put("limit", limit);
        data.put("orderby", orderby);

        PageInfo<Soyuan> pageInfo = soyuanService.querySoyuanAll(data);
        return JsonInfo.ok("querySoyuanAll", Constants.OK_MSG, pageInfo.getPages(), pageInfo.getTotal(), page, pageInfo.getList());
    }


    //查询列表
    @RequestMapping("/topSoyuanNumList")
    @ResponseBody
    public JsonInfo topSoyuanNumList(Soyuan soyuan,
                                     @RequestParam(defaultValue = "0") Integer num,
                                     @RequestParam(defaultValue = "") String whstr,
                                     @RequestParam(defaultValue = "id desc") String orderby) {

        //whstr=whstr+" and id="+id;
        Map<String, Object> data = new HashMap<String, Object>();
        data.put("soyuan", soyuan);
        data.put("limit", num);
        data.put("orderby", orderby);
        data.put("whstr", whstr);
        List<Soyuan> list = soyuanService.topSoyuanNumList(data);
        return JsonInfo.ok("topSoyuanNumList", Constants.OK_MSG, 1, (long) list.size(), 1, list);
    }


    /**
     * 根据id查询
     */
    @RequestMapping("/querySoyuanById")
    @ResponseBody
    public JsonInfo querySoyuanById(Soyuan soyuan, @RequestParam(defaultValue = "0") Integer id) {
        soyuan = soyuanService.querySoyuanById(id);//根据id查询对象
        return JsonInfo.ok("querySoyuanById", Constants.OK_MSG, Arrays.asList(soyuan));
    }


    /**
     * 按ID 删除
     */

    @RequestMapping("/deleteSoyuanByIds")
    @ResponseBody
    public JsonInfo deleteSoyuanByIds(String ids) {
        List<String> list = Arrays.asList(ids.split(","));
        soyuanService.deleteSoyuanByIds(list);
        return JsonInfo.ok("deleteSoyuanByIds", Constants.OK_MSG);
    }


    /**
     * 添加提交
     *
     * @param soyuan
     * @return
     */
    @RequestMapping("/addSoyuanSubmit")
    @ResponseBody
    public JsonInfo addSoyuanSubmit(Soyuan soyuan) {
        String msg = Constants.ERR_MSG;
        try {
            soyuanService.addSoyuanSubmit(soyuan);
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("addSoyuanSubmit", msg);
    }


    /**
     * 修改提交
     */
    @RequestMapping("/updateSoyuanSubmit")
    @ResponseBody
    public JsonInfo updateSoyuanSubmit(Soyuan soyuan) {
        String msg = Constants.ERR_MSG;
        try {
            soyuanService.updateSoyuanSubmit(soyuan);//数据库修改
            msg = Constants.OK_MSG;
        } catch (Exception e) {
            msg = Constants.ERR_MSG;

        }
        return JsonInfo.ok("updateSoyuanSubmit", msg);
    }

    /**
     * 生成二维码并以图片形式返回
     */
    @GetMapping(value = "/qrcode")
    public ResponseEntity<byte[]> getQRCode(@RequestParam(value = "text") String text) {
        try {
            byte[] qrImage = soyuanService.generateQRCodeImage(text, 360, 360);
            return ResponseEntity.status(HttpStatus.OK).contentType(MediaType.IMAGE_PNG).body(qrImage);
        } catch (IOException e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
        }
    }


}
