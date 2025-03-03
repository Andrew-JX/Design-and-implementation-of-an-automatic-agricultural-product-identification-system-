package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.JilvMapper;
import com.shuyuansys.po.Jilv;
import com.shuyuansys.service.JilvService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Map;
import java.util.List;

@Service("jilvService")
public class JilvServiceimpl implements JilvService {

    @Autowired
    private JilvMapper jilvMapper;

    @Override
    public PageInfo<Jilv> queryJilvAll(Map<String,Object> map) {

        int page= (int) map.get("page");
        int limit= (int) map.get("limit");
        PageHelper.startPage(page,limit);

        List<Jilv> jilvList = jilvMapper.queryJilvInfoAll(map);
        return new PageInfo<>(jilvList) ;
    }
  @Override
    public  List<Jilv> topJilvNumList(Map<String,Object> map)
    {
                 List<Jilv> toplist=jilvMapper.topJilvNumList(map);
                 return  toplist;

     }

  @Override
    public  List<Jilv> topJilvNumListInTable(Map<String,Object> map)
        {
        List<Jilv> toplist=jilvMapper.topJilvNumList(map);
        return  toplist;

        }

    @Override
    public void addJilvSubmit(Jilv jilv) {
        jilvMapper.insert(jilv);
    }

    @Override
    public Jilv queryJilvById(Integer id) {
        return jilvMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateJilvSubmit(Jilv jilv) {
        jilvMapper.updateByPrimaryKeySelective(jilv);//修改不为空的字段
    }

    @Override
    public void deleteJilvByIds(List<String> ids) {
        for (String id : ids){
            jilvMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


}
