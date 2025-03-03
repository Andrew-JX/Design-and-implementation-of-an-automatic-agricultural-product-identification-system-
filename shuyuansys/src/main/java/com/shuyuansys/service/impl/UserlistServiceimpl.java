package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.UserlistMapper;
import com.shuyuansys.po.Userlist;
import com.shuyuansys.service.UserlistService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Map;
import java.util.List;

@Service("userlistService")
public class UserlistServiceimpl implements UserlistService {

    @Autowired
    private UserlistMapper userlistMapper;

    @Override
    public PageInfo<Userlist> queryUserlistAll(Map<String,Object> map) {

        int page= (int) map.get("page");
        int limit= (int) map.get("limit");
        PageHelper.startPage(page,limit);

        List<Userlist> userlistList = userlistMapper.queryUserlistInfoAll(map);
        return new PageInfo<>(userlistList) ;
    }
  @Override
    public  List<Userlist> topUserlistNumList(Map<String,Object> map)
    {
                 List<Userlist> toplist=userlistMapper.topUserlistNumList(map);
                 return  toplist;

     }

  @Override
    public  List<Userlist> topUserlistNumListInTable(Map<String,Object> map)
        {
        List<Userlist> toplist=userlistMapper.topUserlistNumList(map);
        return  toplist;

        }

    @Override
    public void addUserlistSubmit(Userlist userlist) {
        userlistMapper.insert(userlist);
    }

    @Override
    public Userlist queryUserlistById(Integer id) {
        return userlistMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateUserlistSubmit(Userlist userlist) {
        userlistMapper.updateByPrimaryKeySelective(userlist);//修改不为空的字段
    }

    @Override
    public void deleteUserlistByIds(List<String> ids) {
        for (String id : ids){
            userlistMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


}
