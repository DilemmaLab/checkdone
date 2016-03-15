function toggleDiv(divId) {
   $("#"+divId).toggle();
}

// Tooltips/hints enabling for Bootstrap tooltips/hints
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

// DatePicker
$(document).ready(function() {
    $('.datepicker').datepicker();
});
// TimePicker
$(document).ready(function() {
    $('.timepicker').timepicker();
});
// DateTimePicker
$(document).ready(function() {
    $('.datetimepicker').datetimepicker();
});

// (Not Implemented Yet)
//AJAX-Delete
function SendPost() {
	//отправляю POST запрос и получаю ответ
	$$a({
		type:'post',//тип запроса: get,post либо head
		url:'',//url адрес файла обработчика
		data:{'z':'1'},//параметры запроса
		response:'text',//тип возвращаемого ответа text либо xml
		success:function (data) {//возвращаемый результат от сервера
			$$('result',$$('result').innerHTML+'<br />'+data);
		}
	});
}
