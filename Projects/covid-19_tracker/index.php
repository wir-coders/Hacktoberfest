<!DOCTYPE html>
<html>

<head>
	<title>CovidIndia</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
	<link href="https://fonts.googleapis.com/css2?family=Muli:wght@300&display=swap" rel="stylesheet">
	<style>
		* {
			margin: 0;
			padding: 0;
			box-sizing: border-box;
			font-family: 'Muli', sans-serif;
		}
 
		.line {
			text-decoration: underline;
		}

		.search-box {
			border: solid #343A40 2px;

		}

		#India {
			width: 25px;

		}

		.corona-update h5 {
			text-decoration: underline;
		}

		@media only screen and (min-width: 480px) {
			.scrollLeft {

				display: none;

			}
		}
	</style>
</head>

<body onload="fetch();">
<?php include('navbar.html');  ?>
	<section class=" corona-update container-fluid">
		<div class="mb-4">
			<h2 class="text-center text-uppercase pt-3 pb-0">COVID-19 LIVE STATS-(India)</h2>
		</div>
		<!--All India-->
		<div class="row text-center">
			<div class="col-md text-dark">
				<h5 class="font-weight-bold pt-0">All Over India</h5>
				<h3 class="count pb-2" id="AOI"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Emblem_of_India.svg/220px-Emblem_of_India.svg.png" id="India"></h3>
			</div>

			<div class="col-md text-info">
				<h5 class="font-weight-bold">Total Confirmed</h5>
				<h3 class="count pb-2" id="TC"></h3>
			</div>

			<div class="col-md text-warning">
				<h5 class="font-weight-bold">Total Active</h5>
				<h3 class="count pb-2" id="TA"></h3>
			</div>

			<div class="col-md text-success">
				<h5 class="font-weight-bold">Total Recovered</h5>
				<h3 class="count pb-2" id="TR"></h3>
			</div>

			<div class="col-md text-danger">
				<h5 class="font-weight-bold">Total Deaths</h5>
				<h3 class="count pb-2" id="TD"></h3>
			</div>

			<div class="col-md col-md-2 col-12">
				<h5 class="font-weight-bold">Last Update</h5>
				<h3 class="count pb-2" id="LU"></h3>
			</div>
		</div>

		<!--SEARCH BOX-->
		<div class="text-center">
			<!--Search box-->
			<input class=" text-center mb-3 pl-5 pr-5 pt-2 pb-2 search-box" type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for States.." title="Search here">
			<p>[Please avoid spaces after name]</p>
			<div class="scrollLeft">
				<p>Scroll left-></p>
			</div>
		</div>
		<!--TABLE HEADING-->
		<div class="text-center table-responsive">
			<table class="table table-bordered table-striped table-dark" id="corona_table">
				<tr>

					<th>State</th>
					<th>Last Update</th>
					<th>Confirmed</th>
					<th>Active</th>
					<th>Recovered</th>
					<th>Deaths</th>
				</tr>
			</table>
		</div>
	</section>
	<!--Access the data statewise from API-->
	<?php
	//this method is working on localhost and not on live web
	// $x=file_get_contents('https://api.covid19india.org/data.json');
	// $json=json_decode($x,true);//decode it using json
	// $state=$json['statewise'];//state data
	// // echo "<pre>";
	// // print_r($state);

	//HERE IS THE ALTERNATIVE OF ABOVE WORK
	$x = 'https://api.covid19india.org/data.json';
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $x);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$content = curl_exec($ch);
	curl_close($ch);
	$json = json_decode($content, true); //decode it using json
	$state = $json['statewise']; //state data -->
	// echo "<pre>";
	// print_r($state);
	// print_r($json)
	?>
	<script type="text/javascript">
		var corona_table = document.getElementById('corona_table'); //take table
		/*Passing php states array to  javascript variable*/
		var state = <?php echo json_encode($state); ?>;
		for (i = 1; i < (state.length); i++) {

			var y = corona_table.insertRow(); //row insert
			//Data insertion
			y.insertCell(0);
			corona_table.rows[i].cells[0].innerHTML = state[i]['state'];

			y.insertCell(1);
			corona_table.rows[i].cells[1].innerHTML = state[i]['lastupdatedtime'];

			y.insertCell(2);
			corona_table.rows[i].cells[2].innerHTML = state[i]['confirmed'];

			y.insertCell(3);
			corona_table.rows[i].cells[3].innerHTML = state[i]['active'];

			y.insertCell(4);
			corona_table.rows[i].cells[4].innerHTML = state[i]['recovered'];

			y.insertCell(5);
			corona_table.rows[i].cells[5].innerHTML = state[i]['deaths'];
		}

		/*All India Data*/
		document.getElementById('TC').innerHTML = state[0]['confirmed'];
		document.getElementById('TA').innerHTML = state[0]['active'];
		document.getElementById('TR').innerHTML = state[0]['recovered'];
		document.getElementById('TD').innerHTML = state[0]['deaths'];
		document.getElementById('LU').innerHTML = state[0]['lastupdatedtime'];
	</script>
	<script>
		/*For search box*/
		function myFunction() {
			var input, filter, table, tr, td, i, txtValue;
			input = document.getElementById("myInput");
			filter = input.value.toUpperCase();
			table = document.getElementById("corona_table");
			tr = table.getElementsByTagName("tr");
			for (i = 0; i < tr.length; i++) {
				td = tr[i].getElementsByTagName("td")[0];
				if (td) {
					txtValue = td.textContent || td.innerText;
					if (txtValue.toUpperCase().indexOf(filter) > -1) {
						tr[i].style.display = "";
					} else {
						tr[i].style.display = "none";
					}
				}
			}
		}
	</script>
	<?php include('footer.html');  ?>
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

	<!-- Popper JS -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>

	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
</body>

</html>