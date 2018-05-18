    function run_module(_accesstoken,_timestamp,_wanip,_moduleName)
    {
        var id = id;
        //_accesstoken = "asdfasdf23esf23easdf23zfas3";
        //复杂一点的json的另一种形式  
        //var value2 = {"user_id":"123456","username":"coolcooldool"};
        //var obj2 = eval(value2);
        
        var postResult = $.post("/runJobBySaltApi/state",{
            accesstoken:_accesstoken,
            timestamp:_timestamp,
            moduleName:_moduleName,
            wanip:_wanip
	        },
	        function(data,status){
	        	//layer.open({
	        	//	 type: 1,
	        	//	 area: ['600px', '360px'],
	        	//	 shadeClose: true, //点击遮罩关闭
	        	//	 content: '<div class="modal-content">  <div class="modal-header">     <h3 class="modal-title"><strong>请求状态</strong></h3>         </div>         <div class="modal-body">            '+status+'        </div>         <div class="modal-footer">             <button type="button" class="btn btn-effect-ripple btn-primary" style="overflow: hidden; position: relative;">参考执行结果</button>     </div>     </div>'
	        	//		 });
	        	window.location.href="select/"+data;
	        }
        );
        if (postResult.status!='200')
    	{
        	alert("请求失败请刷后新重试，当前状态: "+ postResult.status);
    	}
    }
    function run_cmd(_accesstoken,_timestamp,_wanip,_cmdtext)
    {
        var id = id;
        //_accesstoken = "asdfasdf23esf23easdf23zfas3";
        //复杂一点的json的另一种形式  
        //var value2 = {"user_id":"123456","username":"coolcooldool"};
        //var obj2 = eval(value2);
        
        var postResult = $.post("/runJobBySaltApi/cmd",{
            accesstoken:_accesstoken,
            timestamp:_timestamp,
            cmdtext:_cmdtext,
            wanip:_wanip
	        },
	        function(data,status){
	        	//layer.open({
	        	//	 type: 1,
	        	//	 area: ['600px', '360px'],
	        	//	 shadeClose: true, //点击遮罩关闭
	        	//	 content: '<div class="modal-content">  <div class="modal-header">     <h3 class="modal-title"><strong>请求状态</strong></h3>         </div>         <div class="modal-body">            '+status+'        </div>         <div class="modal-footer">             <button type="button" class="btn btn-effect-ripple btn-primary" style="overflow: hidden; position: relative;">参考执行结果</button>     </div>     </div>'
	        	//		 });
	        	window.location.href="cmdrun/"+_wanip+"/"+data;
	        }
        );
        if (postResult.status!='200')
    	{
        	alert("请求失败请刷后新重试，当前状态: "+ postResult.status);
    	}
    }