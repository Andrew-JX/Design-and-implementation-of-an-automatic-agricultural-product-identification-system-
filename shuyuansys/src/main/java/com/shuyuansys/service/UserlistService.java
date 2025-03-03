package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Userlist;

import java.util.List;
import java.util.Map;

public interface UserlistService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Userlist> queryUserlistAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Userlist> topUserlistNumList(Map<String,Object> map);

   List<Userlist> topUserlistNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addUserlistSubmit(Userlist userlist);

    /**
     * 根据id查询（修改）
     */
    Userlist queryUserlistById(Integer id);

    /**
     * 修改提交
     */
    void updateUserlistSubmit(Userlist userlist);

    /**
     * 删除
     */
    void deleteUserlistByIds(List<String> ids);


}
