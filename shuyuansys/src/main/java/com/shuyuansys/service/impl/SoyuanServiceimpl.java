package com.shuyuansys.service.impl;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.shuyuansys.dao.SoyuanMapper;
import com.shuyuansys.po.Soyuan;
import com.shuyuansys.service.SoyuanService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.List;


//二维码生成

import com.google.zxing.WriterException;
import com.google.zxing.qrcode.QRCodeWriter;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import org.springframework.stereotype.Service;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

//-----------

@Service("soyuanService")
public class SoyuanServiceimpl implements SoyuanService {

    @Autowired
    private SoyuanMapper soyuanMapper;

    @Override
    public PageInfo<Soyuan> querySoyuanAll(Map<String, Object> map) {

        int page = (int) map.get("page");
        int limit = (int) map.get("limit");
        PageHelper.startPage(page, limit);

        List<Soyuan> soyuanList = soyuanMapper.querySoyuanInfoAll(map);
        return new PageInfo<>(soyuanList);
    }

    @Override
    public List<Soyuan> topSoyuanNumList(Map<String, Object> map) {
        List<Soyuan> toplist = soyuanMapper.topSoyuanNumList(map);
        return toplist;

    }

    @Override
    public List<Soyuan> topSoyuanNumListInTable(Map<String, Object> map) {
        List<Soyuan> toplist = soyuanMapper.topSoyuanNumList(map);
        return toplist;

    }

    @Override
    public void addSoyuanSubmit(Soyuan soyuan) {
        soyuanMapper.insert(soyuan);
    }

    @Override
    public Soyuan querySoyuanById(Integer id) {
        return soyuanMapper.selectByPrimaryKey(id);
    }

    @Override
    public void updateSoyuanSubmit(Soyuan soyuan) {
        soyuanMapper.updateByPrimaryKeySelective(soyuan);//修改不为空的字段
    }

    @Override
    public void deleteSoyuanByIds(List<String> ids) {
        for (String id : ids) {
            soyuanMapper.deleteByPrimaryKey(Integer.parseInt(id));
        }
    }


    /**
     * 生成二维码图片并以字节数组形式返回
     *
     * @param text   二维码内容
     * @param width  宽度
     * @param height 高度
     * @return 二维码图片的字节数组
     * @throws WriterException
     * @throws IOException
     */
    @Override
    public byte[] generateQRCodeImage(String text, int width, int height) {
        try {
            QRCodeWriter qrCodeWriter = new QRCodeWriter();
            Map<EncodeHintType, Object> hints = new HashMap<>();
            hints.put(EncodeHintType.CHARACTER_SET, "UTF-8");
            BitMatrix bitMatrix = qrCodeWriter.encode(text, BarcodeFormat.QR_CODE, width, height, hints);

            ByteArrayOutputStream pngOutputStream = new ByteArrayOutputStream();
            MatrixToImageWriter.writeToStream(bitMatrix, "PNG", pngOutputStream);
            return pngOutputStream.toByteArray();
        } catch (WriterException | IOException e) {
            // Handle exception: Log it, throw a runtime exception, etc.
            throw new RuntimeException("Error while generating QR Code", e);
        }
    }


}
