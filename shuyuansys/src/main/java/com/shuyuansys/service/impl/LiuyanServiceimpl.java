package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.LiuyanMapper;
import com.shuyuansys.po.Liuyan;
import com.shuyuansys.service.LiuyanService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.List;

@Service("liuyanService")
public class LiuyanServiceimpl implements LiuyanService {

    @Autowired
    private LiuyanMapper liuyanMapper;

    @Override
    public PageInfo<Liuyan> queryLiuyanAll(Map<String, Object> map) {

        int page = (int) map.get("page");
        int limit = (int) map.get("limit");
        PageHelper.startPage(page, limit);

        List<Liuyan> liuyanList = liuyanMapper.queryLiuyanInfoAll(map);
        return new PageInfo<>(liuyanList);
    }

    @Override
    public List<Liuyan> topLiuyanNumList(Map<String, Object> map) {
        List<Liuyan> toplist = liuyanMapper.topLiuyanNumList(map);
        return toplist;

    }

    @Override
    public List<Liuyan> topLiuyanNumListInTable(Map<String, Object> map) {
        List<Liuyan> toplist = liuyanMapper.topLiuyanNumList(map);
        return toplist;

    }

    @Override
    public void addLiuyanSubmit(Liuyan liuyan) {
        liuyanMapper.insert(liuyan);
    }

    @Override
    public Liuyan queryLiuyanById(Integer id) {
        return liuyanMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateLiuyanSubmit(Liuyan liuyan) {
        liuyanMapper.updateByPrimaryKeySelective(liuyan);//修改不为空的字段
    }

    @Override
    public void deleteLiuyanByIds(List<String> ids) {
        for (String id : ids) {
            liuyanMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


}
