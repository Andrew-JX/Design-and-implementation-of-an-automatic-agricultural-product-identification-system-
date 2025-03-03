package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Soyuan;

import java.io.IOException;
import java.util.List;
import java.util.Map;

public interface SoyuanService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Soyuan> querySoyuanAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Soyuan> topSoyuanNumList(Map<String,Object> map);

   List<Soyuan> topSoyuanNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addSoyuanSubmit(Soyuan soyuan);

    /**
     * 根据id查询（修改）
     */
    Soyuan querySoyuanById(Integer id);

    /**
     * 修改提交
     */
    void updateSoyuanSubmit(Soyuan soyuan);

    /**
     * 删除
     */
    void deleteSoyuanByIds(List<String> ids);

    /*生成二维码*/
    byte[] generateQRCodeImage(String text, int width, int height) throws IOException;
}
