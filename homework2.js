<meta charset="utf-8">
<script>
var a = 1, b = 1, c, d;
c = ++a; alert(c);           // 2 здесь используется префиксная форма записи оператора инкрементирования. В этом случае инкрементирование производится сразу и в консоль выводится обновленное значение переменной a, которое и сохраняется в переменной c
d = b++; alert(d);           // 1 В постфиксной форме сначала происходит возвращение значения, а потом выполняется инкрементирование. Поэтому в переменную d записалось начальное значение переменной b - 1
c = (2+ ++a); alert(c);      // 5 в консоль выводится - 4, а не 5: инкрементирование a дает 2, 2 + 2 = 4
d = (2+ b++); alert(d);      // 4 в консоль выводится 3, а не 4: постфиксное инкрементирование возвращает текущее значение
alert(a);                    // 3 на протяжении данного кода операция инкрементирования над переменной a выполнялась 2 раза, поэтому текущее ее значение - 3
alert(b);                    // 3 на протяжении данного кода операция инкрементирования над переменной b выполнялась 2 раза, поэтому текущее ее значение - 3

var a = 2;
var x = 1 + (a *= 2); // x = 5

var a = +prompt('Введите число');
var b =+prompt('Введите число');
if (a > 0 && b > 0){
	document.write(a - b);
	}
else if (a < 0 && b < 0){
	document.write(b * a);
	}
else if (a < 0 && b > 0){
	document.write(a + b);
	}

// как С помощью оператора switch организовать вывод чисел от a до 15 не понял.

function add(number1, number2){

	return number1 + number2;
}

document.write(add(1,2));

function diminution(number1, number2){
	return number1 - number2;
}

document.write(diminution(4,1));

function multiple(number1, number2){
	return number1 * number2;
}

document.write(multiple(2,2));

function division(number1, number2){
	return number1 / number2;
}

document.write(division(8,2));

function add(number1, number2){
	return number1 + number2;
}

function diminution(number1, number2){
	return number1 - number2;
}

function multiple(number1, number2){
	return number1 * number2;
}

function division(number1, number2){
	return number1 / number2;
}

function mathOperation(arg1, arg2, operation){
	switch (operation){
		case 'add':
		document.write(add(arg1, arg2));
		break;
		case 'diminution':
		document.write(diminution(arg1, arg2));
		break;
		case 'multiple':
		document.write(multiple(arg1, arg2));
		break;
		case 'division':
		document.write(division(arg1, arg2));
		break;
}
}

mathOperation(3, 3, 'multiple');
</script>