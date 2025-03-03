package com.shuyuansys.controller;

import com.github.pagehelper.PageInfo;

import com.shuyuansys.utils.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;
import javax.servlet.http.HttpServletRequest;

import org.springframework.util.ClassUtils;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;

import java.util.UUID;


@Controller
public class BaseController {

    /**
     * 上传
     *
     * @return
     */

    @GetMapping("/upload")
    public String upload(HttpServletRequest request) {
        String f = "";
        f = request.getParameter("f");
        System.out.println(f);
        request.setAttribute("f", f);
        return "upload";
    }

    @ResponseBody
    @RequestMapping(value = "/doUploadjson", method = RequestMethod.POST)
    public JsonInfo doUploadvue(@RequestParam("file") MultipartFile file) throws FileNotFoundException {

        String basePath = ClassUtils.getDefaultClassLoader().getResource("").getPath() + "static";
        System.out.println("upload url:" + basePath);
        //重新定义文件名、避免名称重复

        String fname = file.getOriginalFilename();
        int pos = fname.lastIndexOf(".");

        if (pos > 0) {
            fname = fname.substring(pos, fname.length());

        }


        String fileName = UUID.randomUUID().toString().replace("-", "").substring(0, 15) + "" + fname;
        //上传文件至指定位置
        String disk = basePath;
        String dicr = "upload";
        File newFlieDic = new File(disk + File.separator + dicr);
        if (!newFlieDic.exists()) {
            newFlieDic.mkdirs();
        }
        File newfile = new File(newFlieDic.getPath(), fileName);
        try {
            file.transferTo(newfile);
        } catch (IOException ioException) {
            ioException.printStackTrace();
        }


        return JsonInfo.ok("doUpload", Constants.OK_MSG, Arrays.asList(fileName));


    }

}
