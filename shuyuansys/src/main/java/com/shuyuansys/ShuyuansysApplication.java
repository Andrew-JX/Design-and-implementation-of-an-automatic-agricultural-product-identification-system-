package com.shuyuansys;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScans;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;


@ComponentScans(value = {
        @ComponentScan("com.shuyuansys.controller"),
        @ComponentScan("com.shuyuansys.service.impl")
})



@SpringBootApplication
@MapperScan("com.shuyuansys.dao")
public class ShuyuansysApplication {

    public static void main(String[] args) {
        SpringApplication.run(ShuyuansysApplication.class, args);
    }

}

@Configuration
class WebMvcConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/static/**").addResourceLocations("classpath:/static/").addResourceLocations("classpath:/static/");
    }
}