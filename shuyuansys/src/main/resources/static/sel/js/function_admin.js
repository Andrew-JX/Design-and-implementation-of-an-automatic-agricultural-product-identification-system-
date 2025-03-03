 


var domainw = window.location.host;
var urlstr="http://"+domainw+"/";
 
function chktel(tel)
{
    var  re = /^1\d{10}$/;
    if (re.test(tel)) {
       return 1;
    } else {
        return 0;
    }
}

 
function gogo(urlstr1)
 {
	 
	 
	 location=urlstr1;
								
	 
	 
	 
	 }
 
	 function goblack()
 {
	 
	 history.back();

	 
	 }

function get(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
	var r = window.location.search.substr(1).match(reg);
	if (r != null) return unescape(r[2]); return null;
}

	  function set_select_checked(selectId, checkValue){  
		    var select = document.getElementById(selectId);  
		 
		    for (var i = 0; i < select.options.length; i++){  
		        if (select.options[i].value == checkValue){  
		            select.options[i].selected = true;  
		            break;  
		        }  
		    }  
		} 
	  
	 function get_select_checked(selectId){  
		    var myselect = document.getElementById(selectId);  
		    var index=myselect.selectedIndex ;
		   return myselect.options[index].value;
		    
		} 

    function refresh()
    {
		window.location.reload();
    }



	function zma(str)
	{
		return str;
	}



iflogin();
function iflogin()
{
	$.ajax({
		type: "post",
		dataType: "json",
		data:null,
		url: "/useradmin/UseradminGetLogin",
		success: function(data){
			if(data.msg=='000001')
			{
				top.location.href="../../web/admin/login.html"
			}
			else
			{  try{
				document.getElementById('username').innerHTML= data.msg
					}
					catch(err)
					{

					}

			}
		},
		error: function(msg){


		}
	});


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
