package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.UseradminMapper;
import com.shuyuansys.po.Useradmin;
import com.shuyuansys.service.UseradminService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.List;

@Service("useradminService")
public class UseradminServiceimpl implements UseradminService {

    @Autowired
    private UseradminMapper useradminMapper;

    @Override
    public PageInfo<Useradmin> queryUseradminAll(Map<String, Object> map) {

        int page = (int) map.get("page");
        int limit = (int) map.get("limit");
        PageHelper.startPage(page, limit);

        List<Useradmin> useradminList = useradminMapper.queryUseradminInfoAll(map);
        return new PageInfo<>(useradminList);
    }

    @Override
    public List<Useradmin> topUseradminNumList(Map<String, Object> map) {
        List<Useradmin> toplist = useradminMapper.topUseradminNumList(map);
        return toplist;

    }

    @Override
    public List<Useradmin> topUseradminNumListInTable(Map<String, Object> map) {
        List<Useradmin> toplist = useradminMapper.topUseradminNumList(map);
        return toplist;

    }

    @Override
    public void addUseradminSubmit(Useradmin useradmin) {
        useradminMapper.insert(useradmin);
    }

    @Override
    public Useradmin queryUseradminById(Integer id) {
        return useradminMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateUseradminSubmit(Useradmin useradmin) {
        useradminMapper.updateByPrimaryKeySelective(useradmin);//修改不为空的字段
    }

    @Override
    public void deleteUseradminByIds(List<String> ids) {
        for (String id : ids) {
            useradminMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


}
