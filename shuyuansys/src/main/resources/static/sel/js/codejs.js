 function strTrim(str) {
        str = str.replace(/(^\s*)|(\s*$)/g, "");     
        return str;     
    }   
    function zma(str) {
      //  str = strTrim(str);
      //  return escape(str).replace(/\%/g,'\\');
        return str;
    }  
    function jiema(str) {
        str = strTrim(str);  
        return unescape(str.replace(/\\/g,'%'));  
    }


 function getQueryString(name) {
     var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
     var r = window.location.search.substr(1).match(reg);
     if (r != null)
         return decodeURIComponent(r[2]);
     return null;
 }

 function getding()
 {  var sNow="";
     var vNow = new Date();
     sNow += String(vNow.getFullYear());
     sNow += String(vNow.getMonth() + 1);
     sNow += String(vNow.getDate());
     sNow += String(vNow.getHours());
     sNow += String(vNow.getMinutes());
     sNow += String(vNow.getSeconds());
     sNow += String(vNow.getMilliseconds());
     return sNow;
 }
 function uptime()
 {

     var date = new Date();
     var seperator1 = "-";
     var seperator2 = ":";
     //以下代码依次是获取当前时间的年月日时分秒
     var year = date.getFullYear();
     var month = date.getMonth() + 1;
     var strDate = date.getDate();
     var minute = date.getMinutes();
     var hour = date.getHours();
     var second = date.getSeconds();
     //固定时间格式
     if (month >= 1 && month <= 9) {
         month = "0" + month;
     }
     if (strDate >= 0 && strDate <= 9) {
         strDate = "0" + strDate;
     }
     if (hour >= 0 && hour <= 9) {
         hour = "0" + hour;
     }
     if (minute >= 0 && minute <= 9) {
         minute = "0" + minute;
     }
     if (second >= 0 && second <= 9) {
         second = "0" + second;
     }
     var currentdate =  year + seperator1 + month + seperator1 + strDate
         + " " + hour + seperator2 + minute + seperator2 + second;
     //getFullYear() 年
     //getMonth()+1 月
     //getDate() 日
     //getHours() 时
     //getMinutes() 分
     //getSeconds() 秒
     console.log(currentdate);
     return currentdate;




 }

 function istel(tel)
    {
        var  re = /^1\d{10}$/;
        if (re.test(tel)) {
           return true;
        } else {
            return false;
        }
    }
      
    
    
    function isemail(emailInput) {
    	   var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    	   if (!myreg.test(emailInput)) {
    	       return false;
    	   }
    	   else {
    	       return true;
    	   }
    	}


 String.prototype.replaceAll = function (FindText, RepText) {
     var regExp = new RegExp(FindText, "g");
     return this.replace(regExp, RepText);
 }



 function htmlDecode(str) {
     return str.replace(/\&quot;/g,"\"").replace(/\&lt;/g,"<").replace(/\&gt;/g,">").replace(/\&nbsp;/g," ").replace(/\&amp;/g,"&");
 }