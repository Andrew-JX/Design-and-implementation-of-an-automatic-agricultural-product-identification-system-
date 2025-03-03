package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.WenfeiMapper;
import com.shuyuansys.po.Wenfei;
import com.shuyuansys.service.WenfeiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.Map;
import java.util.List;

@Service("wenfeiService")
public class WenfeiServiceimpl implements WenfeiService {

    @Autowired
    private WenfeiMapper wenfeiMapper;

    @Override
    public PageInfo<Wenfei> queryWenfeiAll(Map<String,Object> map) {

        int page= (int) map.get("page");
        int limit= (int) map.get("limit");
        PageHelper.startPage(page,limit);

        List<Wenfei> wenfeiList = wenfeiMapper.queryWenfeiInfoAll(map);
        return new PageInfo<>(wenfeiList) ;
    }
  @Override
    public  List<Wenfei> topWenfeiNumList(Map<String,Object> map)
    {
                 List<Wenfei> toplist=wenfeiMapper.topWenfeiNumList(map);
                 return  toplist;

     }

  @Override
    public  List<Wenfei> topWenfeiNumListInTable(Map<String,Object> map)
        {
        List<Wenfei> toplist=wenfeiMapper.topWenfeiNumList(map);
        return  toplist;

        }

    @Override
    public void addWenfeiSubmit(Wenfei wenfei) {
        wenfeiMapper.insert(wenfei);
    }

    @Override
    public Wenfei queryWenfeiById(Integer id) {
        return wenfeiMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateWenfeiSubmit(Wenfei wenfei) {
        wenfeiMapper.updateByPrimaryKeySelective(wenfei);//修改不为空的字段
    }

    @Override
    public void deleteWenfeiByIds(List<String> ids) {
        for (String id : ids){
            wenfeiMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


}
