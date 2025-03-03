package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Wenfei;

import java.util.List;
import java.util.Map;

public interface WenfeiService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Wenfei> queryWenfeiAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Wenfei> topWenfeiNumList(Map<String,Object> map);

   List<Wenfei> topWenfeiNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addWenfeiSubmit(Wenfei wenfei);

    /**
     * 根据id查询（修改）
     */
    Wenfei queryWenfeiById(Integer id);

    /**
     * 修改提交
     */
    void updateWenfeiSubmit(Wenfei wenfei);

    /**
     * 删除
     */
    void deleteWenfeiByIds(List<String> ids);


}
