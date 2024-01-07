(function(){
	$(function(){
		console.log('ura!');

		$('#ok').on('click',function(){
			
			var data = $('#form').serialize();
			$.ajax({
			    type: "POST",
			    url: "/getData",
			    data: data,
			    beforeSend: function(){
			       
			    },
			    success: function(answer){
			        console.log(answer);
			    },
			    error:function(){
			        
			    }
			});
		});
	});
})();




