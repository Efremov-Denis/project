<meta charset="utf-8">
<script>
// С первой задачей проблемып
function countBasketPrice(articles){
	let result = 0;
	for (num in articles)
{
		result += num
	}
	return result
}

document.write(countBasketPrice([1,2,3]));
/* в браузер выводится какая-то ерунда,
хотя для python этот код отрабатывает правильно */
</script>