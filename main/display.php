<html>
<style>
*{
   font-size:30px;
}

table, tr, td, th{
   border: 1px solid black;
   text-align:center;
}

table{
   width:30%;
   border-collapse:collapse
}

</style>
<body>

<?php
function jj_readcsv($filename) {
$handle = fopen($filename, "r");
echo '<table>';

echo '<tr><th>Date</th><th>Time</th><th>Name</th></tr>';
// displaying contents
while ($csvcontents = fgetcsv($handle)) {
    echo '<tr>';
    foreach ($csvcontents as $column) {
        echo "<td>$column</td>";
    }
    echo '</tr>';
}
echo '</table>';
fclose($handle);
}

$file = 'db/'.$_GET['file_name'];
jj_readcsv($file);
?>

</body>
</html>
