




var createAjax = function(){
	
	
	
    var xhr=null;
	
	 
	
	
		var xmlHttp=null;
	   try {  
                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP"); // ie msxml3.0+（IE7.0及以上）  
            } catch (e) {  
                try {  
                    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP"); //ie msxml2.6（IE5/6�? 
                } catch (e2) {  
                    xmlHttp = false;  
                }  
            }  
            if (!xmlHttp && typeof XMLHttpRequest != 'undefined') {// Firefox, Opera 8.0+, Safari  
                xmlHttp = new XMLHttpRequest();  
            }  
	
	
	 
	xhr=xmlHttp;
	
    return xhr;
};
var ajax=function(conf){
    var type=conf.type; // type参数,可�?
    var url=conf.url; // url参数，必�?
    var data=conf.data; // data参数可选，只有在post请求时需�?
    var dataType=conf.dataType; // datatype参数可�?
    var success=conf.success; // 回调函数可�?
    if (type == null) {
        type="get"; // type参数可选，默认为get
    }
    if (dataType == null){
        dataType="text"; // dataType参数可选，默认为text
    }
    var xhr = createAjax();
    xhr.open(type,url,true);
    if (type=="GET" || type=="get") {
        xhr.send(null);
    } else if (type=="POST" || type=="post") {
        xhr.setRequestHeader("content-type","application/x-www-form-urlencoded");
        xhr.send(data);
    }
    xhr.onreadystatechange=function(){
        if ((xhr.readyState == 4) && (xhr.status == 200)) {
            if (dataType=="text" || dataType=="TEXT"){
                if (success != null){
                    success(xhr.responseText); // 普通文�?
                }
            } else if(dataType=="xml" || dataType=="XML"){
                if (success != null){
                    success(xhr.responseXML); // 接收xml文档
                }
            } else if (dataType=="json" || dataType=="JSON"){
                if (success != null) {
                    success(eval("("+xhr.responseText+")")); //将json字符串转换为js对象
                }
            }
        }
    };
}; 








function loadimg(iid)
{
	 document.getElementById(iid).innerHTML= "loading...";
	
	
	
}



//清除
function cleart(iid)
{
	 document.getElementById(iid).innerHTML= "";
	
	
	
}

 function strTrim(str) {     
        str = str.replace(/(^\s*)|(\s*$)/g, "");     
        return str;     
    }   
    function zma(str) {
        str = strTrim(str);  
        return escape(str).replace(/\%/g,'\\');  
    }  
    function jiema(str) {
        str = strTrim(str);  
        return unescape(str.replace(/\\/g,'%'));  
    } 






