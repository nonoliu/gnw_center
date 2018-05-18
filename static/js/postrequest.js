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
	        	window.location.href="/editsingle/select/"+data;
	        }
        );
        if (postResult.status!='200')
    	{
        	alert("请求失败请刷后新重试，当前状态: "+ postResult.status);
    	}
    }
    function routeact(_accesstoken,_timestamp,_wanip,_action)
    {
        var id = id;
        var postResult = $.post("/api/routestatus",{
            accesstoken:_accesstoken,
            timestamp:_timestamp,
            wanip:_wanip,
			action:_action
	        },
	        function(data,status){
	        	window.location.href="/manager/route";
	        }
        );
    }
    function serveract(_accesstoken,_timestamp,_wanip,_action)
    {
        var id = id;
        var postResult = $.post("/api/serverstatus",{
            accesstoken:_accesstoken,
            timestamp:_timestamp,
            wanip:_wanip,
			action:_action
	        },
	        function(data,status){
	        	window.location.href="/manager/server";
	        }
        );
    }
	function changewz(_accesstoken,_timestamp,_wanip,_wz)
    {
        var id = id;
        var postResult = $.post("/api/changewz",{
            accesstoken:_accesstoken,
            timestamp:_timestamp,
            wanip:_wanip,
			wz:_wz
	        },
	        function(data,status){
	        	window.location.href="/manager/server";
	        }
        );
    }
	
    function add_server(_accesstoken,_timestamp,_watch,_agent,_zone,_address)
    {
        var id = id;
        var postResult = $.post("/api/addserver",{
            accesstoken:_accesstoken,
            timestamp:_timestamp,
            watch:_watch,
            agent:_agent,
            zone:_zone,
            address:_address
	        },
	        function(data,status){
	        	window.location.href="/manager/server";
	        	//alert("结果: "+ data);
	        	//window.location.reload();
	        }
        );
        
    }