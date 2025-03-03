package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Liuyan;

import java.util.List;
import java.util.Map;

public interface LiuyanService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Liuyan> queryLiuyanAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Liuyan> topLiuyanNumList(Map<String,Object> map);

   List<Liuyan> topLiuyanNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addLiuyanSubmit(Liuyan liuyan);

    /**
     * 根据id查询（修改）
     */
    Liuyan queryLiuyanById(Integer id);

    /**
     * 修改提交
     */
    void updateLiuyanSubmit(Liuyan liuyan);

    /**
     * 删除
     */
    void deleteLiuyanByIds(List<String> ids);


}
