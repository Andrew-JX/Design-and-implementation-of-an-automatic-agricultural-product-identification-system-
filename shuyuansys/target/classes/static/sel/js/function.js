 


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
function soso()
{
var sokey=document.getElementById("sokey").value;
 sokey=encodeURI(sokey);
 
location=urlstr+"/static/web/qian/search/?key="+sokey;
	

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



