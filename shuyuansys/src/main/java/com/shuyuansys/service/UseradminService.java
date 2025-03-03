package com.shuyuansys.service;

import com.github.pagehelper.PageInfo;
import com.shuyuansys.po.Useradmin;

import java.util.List;
import java.util.Map;

public interface UseradminService {

    /**
     * 查询所有列表（分页）
     */
    PageInfo<Useradmin> queryUseradminAll(Map<String,Object> map);
 /**
     * 查询top num
     */

    List<Useradmin> topUseradminNumList(Map<String,Object> map);

   List<Useradmin> topUseradminNumListInTable(Map<String,Object> map);


    /**
     * 添加提交
     */
    void addUseradminSubmit(Useradmin useradmin);

    /**
     * 根据id查询（修改）
     */
    Useradmin queryUseradminById(Integer id);

    /**
     * 修改提交
     */
    void updateUseradminSubmit(Useradmin useradmin);

    /**
     * 删除
     */
    void deleteUseradminByIds(List<String> ids);


}
