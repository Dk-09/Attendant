<html>
<style>
*{
   font-family: Arial;
   font-size: 20px;
}

a{
   text-decoration:none;
}

</style>
<body>


<?php

$fileList = glob('db/*');
foreach($fileList as $filename){
	if(is_file($filename)){
		$file = substr($filename,3);
		echo "<a href='display.php?file_name={$file}'>{$file}</a><br><br>";
    }   
}
?>


</body>
</html>


