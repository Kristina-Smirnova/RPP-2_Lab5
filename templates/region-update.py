<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Изменение региона</title>
</head>
{# templates/region-add.html #}
<body>
    <form action="" method="post">
    {{form.hidden_tag()}}
		<P>{{form.id.label()}} {{form.id()}}</P>
		<p>{{form.name.label()}} {{form.name()}}</p>
		<p>{{form.submit()}}</p>
    </form>
</body>
</html>
