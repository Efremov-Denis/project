<meta charset="utf-8">
<script>
function number_to_object(number){
	let counter = number / 10;
	let digits = number % 10;
	let tens = counter % 10;
	let hundreeds = counter / 10;

	let object_number ={
		'hundreeds': hundreeds,
		'tens': tens,
		'digits': digits
	}
	if (number > 999){
		document.write(prompt('Введите число от 0 до 999'));
		let empty_object = {};
}
	else{
		document.write(object_number);
	}
}
number_to_object(234);
</script>