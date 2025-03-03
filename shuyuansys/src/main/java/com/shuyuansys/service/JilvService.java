package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Jilv;

import java.util.List;
import java.util.Map;

public interface JilvService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Jilv> queryJilvAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Jilv> topJilvNumList(Map<String,Object> map);

   List<Jilv> topJilvNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addJilvSubmit(Jilv jilv);

    /**
     * 根据id查询（修改）
     */
    Jilv queryJilvById(Integer id);

    /**
     * 修改提交
     */
    void updateJilvSubmit(Jilv jilv);

    /**
     * 删除
     */
    void deleteJilvByIds(List<String> ids);


}
